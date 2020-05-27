from django.contrib import admin

from .models import *


class ProductInline(admin.TabularInline):
    model = ProductInOrder
    extra = 1


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'customer_phone', 'created']
    inlines = [ProductInline]


@admin.register(ProductInOrder)
class AdminProductInOrder(admin.ModelAdmin):
    list_display = ['order', 'product', 'created']


@admin.register(ProductBasket)
class AdminProductBasket(admin.ModelAdmin):
    list_display = ['product', 'created']