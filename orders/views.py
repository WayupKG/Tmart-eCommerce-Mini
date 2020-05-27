from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import View, TemplateView, ListView

from .models import *
from products.models import Product


class Basket_Add(View):
    def post(self, request, *args, **kwargs):
        return_dict = dict()
        session_key = request.session.session_key
        data = request.POST
        product_id = data.get('product_id')
        nmb = data.get('nmb')
        product_price = data.get('product_price')
        delete = data.get('delete')

        if delete == 'true':
            pr = ProductBasket.objects.get(id=product_id, session_key=session_key)
            pr.delete()

        else:
            new_product, created = ProductBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                   defaults={'number': nmb, 'price': product_price})
            if not created:
                new_product.price = product_price
                new_product.number = nmb
                new_product.save()

        products_basket = ProductBasket.objects.filter(session_key=session_key)
        products_basket_count = ProductBasket.objects.filter(session_key=session_key).count()
        return_dict['products_basket_count'] = products_basket_count
        return_dict['products'] = list()

        for item in products_basket:
            product_dict = dict()
            product_dict['id'] = item.id
            product_dict['name'] = item.product.name
            product_dict['price'] = item.price
            product_dict['total_price'] = item.total_price
            product_dict['nmb'] = item.number
            product_dict['url'] = item.product.get_absolute_url()
            for img in item.product.img.all():
                if img.is_main == True:
                    product_dict['img'] = img.image.url
            return_dict['products'].append(product_dict)

        basket_total = 0
        for basket in products_basket:
            basket_total += basket.total_price

        return_dict['basket_total_price'] = basket_total

        return JsonResponse(return_dict)


class Card(TemplateView):
    template_name = 'orders/cart.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        products_basket = ProductBasket.objects.filter(session_key=session_key)

        basket_total = 0
        for basket in products_basket:
            basket_total += basket.total_price

        return render(request, self.template_name, {'products_basket': products_basket, 'basket_total': basket_total})

