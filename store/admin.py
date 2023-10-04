from django.contrib import admin
from store import models as store_models

@admin.register(store_models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


@admin.register(store_models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price' ,'digital']

@admin.register(store_models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['complete', 'transaction_id']

@admin.register(store_models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['quantity' ,'date_added']
    
@admin.register(store_models.ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['address' ,'city' ,'zipcode']