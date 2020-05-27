from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class ShopView(ListView):
    template_name = 'shop/shop-sidebar.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        categories = Category.objects.all()
        return render(request, self.template_name, {'products': products,
                                                    'categories': categories})


class ProductDetail(DetailView):
    template_name = 'shop/product-detail.html'
    model = Product
    slug_field = 'slug'
