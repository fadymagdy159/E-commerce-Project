from django.contrib import admin
from .models import OrderItem, Product, Category

admin.site.register(Product)
admin.site.register(Category)
from .models import Order

admin.site.register(Order)
admin.site.register(OrderItem)

