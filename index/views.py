from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models.customers import Customer


class IndexView(View):
    def get(self, request):
        return render(request, 'index/pages/index.html')


class CustomersListView(ListView):
    model = Customer
    template_name = 'index/pages/customer_list.html'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'index/pages/customer_detail.html'
