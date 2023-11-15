from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models.customers import Customer
from .forms import CustomerForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index/pages/index.html')


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
