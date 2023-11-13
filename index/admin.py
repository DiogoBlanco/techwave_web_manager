from django.contrib import admin
from .models.customers import Customer


class CustomerAdmin(admin.ModelAdmin):
    admin.site.register(Customer)
