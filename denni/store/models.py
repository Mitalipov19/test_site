from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from unicodedata import category


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0)
    phone_number = PhoneNumberField(region='KG')
    date_registered = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name


class Shoes(models.Model):
    brand = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=32)
    size = models.IntegerField()
    description = models.TextField()
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    video = models.FileField(upload_to='shoes_videos/', verbose_name='Видео', null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.brand

class ShoesPhotos(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='imades/')

    def __str__(self):
        return f'{self.shoes}'

class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='cart')
    created_date = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    def str(self):
        return f'{self.created_date}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity
