from django.urls import path

from . import views

urlpatterns = [
    path('card/', views.Card.as_view(), name='card'),
    path('basket_add/', views.Basket_Add.as_view(), name='basket_add'),
]
