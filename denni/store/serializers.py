from rest_framework import serializers
from .models import *

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone_number']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    date_registered = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'age', 'phone_number', 'date_registered']


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class ShoesPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoesPhotos
        fields = ['image']


class ShoesListSerializer(serializers.ModelSerializer):
    photos = ShoesPhotosSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Shoes
        fields = ['id', 'brand', 'category', 'price', 'photos', 'active']


class ShoesDetailSerializer(serializers.ModelSerializer):
    photos = ShoesPhotosSerializer(many=True, read_only=True)
    owner = UserProfileSimpleSerializer()
    date = serializers.DateField(format='%d-%m-%Y')
    category = CategorySerializer()

    class Meta:
        model = Shoes
        fields = ['brand', 'category', 'price', 'photos', 'color', 'size', 'description',
                  'date', 'active', 'product_video', 'owner']


class CartItemSerializer(serializers.ModelSerializer):
    product = ShoesListSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Shoes.objects.all(), write_only=True, source='product')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'get_total_price']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']


    def get_total_price(self, obj):
        return obj.get_total_price()