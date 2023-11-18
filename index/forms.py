from django.forms import ModelForm
from .models.customers import Customer
from .models.suppliers import Supplier
from .models.products import Product


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
