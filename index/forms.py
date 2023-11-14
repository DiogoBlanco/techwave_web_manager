from django.forms import ModelForm
from .models.customers import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
