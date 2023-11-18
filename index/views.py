from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models.customers import Customer
from .models.suppliers import Supplier
from .models.products import Product
from .forms import CustomerForm, SupplierForm, ProductForm


# Home
class IndexView(View):
    def get(self, request):
        return render(request, 'index/pages/index.html')


# Customers Views
class CustomersListView(ListView):
    model = Customer
    template_name = 'index/pages/customer_list.html'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'index/pages/customer_detail.html'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = '/customers/'
    template_name = 'index/pages/customer_form.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    success_url = '/customers/'
    template_name = 'index/pages/customer_form.html'


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = '/customers/'
    template_name = 'index/pages/customer_confirm_delete.html'


# Suppliers Views
class SuppliersListView(ListView):
    model = Supplier
    template_name = 'index/pages/supplier_list.html'


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'index/pages/supplier_detail.html'


class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    success_url = '/suppliers/'
    template_name = 'index/pages/supplier_form.html'


class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    success_url = '/suppliers/'
    template_name = 'index/pages/supplier_form.html'


class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = '/suppliers/'
    template_name = 'index/pages/supplier_confirm_delete.html'


# Products Views
class ProductsListView(ListView):
    model = Product
    template_name = 'index/pages/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'index/pages/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = '/products/'
    template_name = 'index/pages/product_form.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = '/products/'
    template_name = 'index/pages/product_form.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/'
    template_name = 'index/pages/product_confirm_delete.html'
