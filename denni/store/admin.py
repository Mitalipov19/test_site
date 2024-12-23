from django.contrib import admin
from .models import *

class ShoesPhotosInline(admin.TabularInline):
    model = ShoesPhotos
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ShoesPhotosInline]


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Shoes, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)