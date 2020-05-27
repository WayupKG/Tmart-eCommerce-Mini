from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView

from products.models import *
from orders.models import ProductBasket


class IndexView(TemplateView):
    template_name = 'leading/index.html'

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()

        return render(request, self.template_name, {'products': products,
                                                    'categories': categories})
