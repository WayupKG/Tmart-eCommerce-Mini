from django.db.models import *
from django.urls import reverse


class Category(Model):
    name = CharField(max_length=50, db_index=True)
    slug = SlugField(max_length=80, unique=True)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    STATUS_STOCK = (
        ('Нет', 'Нет'),
        ('Да', 'Да')
    )

    name = CharField('Называние', max_length=240, db_index=True)
    slug = SlugField(max_length=280, unique=True)
    description = TextField('Описание')
    price = IntegerField('Цена')
    category = ForeignKey(Category, on_delete=CASCADE, related_name='products')
    status_stock = CharField('Есть ли акция на товар', max_length=5, choices=STATUS_STOCK, default='Нет')
    stock_pr = IntegerField(verbose_name="Процент акции", blank=True, null=True, default=0)
    price_stock = IntegerField(verbose_name="Цена акции", blank=True, null=True, default=0)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    status = CharField(max_length=15, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    def save(self, *args, **kwargs):
        res_pro = int(self.price) / 100
        print(res_pro, '-----------')
        res_stock = res_pro * int(self.stock_pr)
        res_price = int(self.price) - res_stock
        self.price_stock = res_price
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ImageProduct(Model):
    product = ForeignKey(Product, on_delete=CASCADE, blank=True, null=True, default=None, related_name='img')
    is_main = BooleanField(verbose_name='Основной картинка', default=False)
    image = ImageField(upload_to='products/%Y/%m/')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображении'
