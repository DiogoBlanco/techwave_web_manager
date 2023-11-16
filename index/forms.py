from django.forms import ModelForm
from .models.customers import Customer
from .models.suppliers import Supplier


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
