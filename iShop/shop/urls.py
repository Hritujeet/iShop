from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tracker', views.tracker, name='tracker'),
    path('products/productView/<str:slug>', views.productView, name='productView'),
    path('checkout', views.checkout, name='checkout'),
    path('addItem', views.addToCart, name='addItem'),
    path('removeCart', views.removeCart, name='removeCart'),
    path('myCart', views.myCart, name='myCart'),
    path('orders', views.orders, name='orders'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
