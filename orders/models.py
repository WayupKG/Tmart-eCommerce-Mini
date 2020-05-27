from django.db import models
from django.db.models.signals import post_save

from products.models import Product


class ProductBasket(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='product_basket', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket')
    session_key = models.CharField('session_key', max_length=250)
    number = models.IntegerField('Количество', default=1)
    price = models.IntegerField(verbose_name='Цена за единицу', default=0)
    total_price = models.IntegerField(verbose_name='Сумма', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.order} - {self.product.name}'

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def save(self, *args, **kwargs):
        self.total_price = int(self.number) * int(self.price)
        super(ProductBasket, self).save(*args, **kwargs)


class Order(models.Model):
    total_price = models.DecimalField(verbose_name='Итого', max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=100, blank=True, null=True, default=None)
    customer_comment = models.TextField('Коментарии')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer_name} - {self.customer_phone}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='product' )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
    number = models.IntegerField('Количество', default=1)
    product_price = models.DecimalField(verbose_name='Цена за единицу', max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(verbose_name='Сумма', max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.order} - {self.product.name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def save(self, *args, **kwargs):
        price = self.product.price
        num = self.number
        self.product_price = price
        self.total_price = int(price) * int(num)

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)
