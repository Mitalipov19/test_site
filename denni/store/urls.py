from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('', ShoesListViewSet.as_view({'get': 'list', 'post': 'create'}), name='shoes_list'),
    path('<int:pk>/', ShoesDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='shoes_detail'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='user_detail'),

    path('photos/', ShoesPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='photos_list'),
    path('photos/<int:pk>/', ShoesPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='photos_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='category_detail'),

    path('cart/', CartViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_list'),
    path('cart/<int:pk>/', CartViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='cart_detail'),

    path('cart_item/', CartItemVewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_item_list'),
    path('cart_item/<int:pk>/', CartItemVewSet.as_view({'get': 'retrieve', 'put': 'update',
                                            'delete': 'destroy'}), name='cart_item_detail'),
]