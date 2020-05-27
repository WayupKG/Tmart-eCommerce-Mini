from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShopView.as_view(), name='shop'),
    path('product/<slug:slug>/', views.ProductDetail.as_view(), name='product'),
]