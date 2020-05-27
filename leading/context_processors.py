from products.models import Product, Category


def getting_product_info(request):
    new_product_3 = Product.objects.all().order_by('-created')[:3]

    month = {1: 'Января', 2: 'Февраля', 3: 'Марта', 4: 'Апреля', 5: 'Мая', 6: 'Июня', 7: 'Июля', 8: 'Августа',
             9: 'Сентября', 10: 'Октября', 11: 'Ноября', 12: 'Декабря', }

    categories = Category.objects.all()[:5]

    return locals()
