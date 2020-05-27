from django.contrib import admin

from .models import *


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'created']
    prepopulated_fields = {'slug': ('name',)}


class ProductImage(admin.TabularInline):
    model = ImageProduct
    extra = 1


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated', 'status']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImage]


@admin.register(ImageProduct)
class AdminProduct(admin.ModelAdmin):
    list_display = ['product']
