from django.contrib import admin
from .models.customers import Customer
from .models.suppliers import Supplier
from .models.products import Product


class CustomerAdmin(admin.ModelAdmin):
    admin.site.register(Customer)


class SupplierAdmin(admin.ModelAdmin):
    admin.site.register(Supplier)


class ProductAdmin(admin.ModelAdmin):
    admin.site.register(Product)
