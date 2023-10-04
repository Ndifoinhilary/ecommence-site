from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('checkout/', views.chectout, name='checkout'),
    path('cart/', views.cart, name='cart'),
]
