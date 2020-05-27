from .models import ProductBasket


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_basket = ProductBasket.objects.filter(session_key=session_key)
    products_basket_count = ProductBasket.objects.filter(session_key=session_key).count()
    basket_total = 0
    for basket in products_basket:
        basket_total += basket.total_price

    return locals()