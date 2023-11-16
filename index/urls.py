from django.urls import path
from .views import *

app_name = 'index'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('customers/', CustomersListView.as_view(), name='customers'),
    path('customers/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/update',
         CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete',
         CustomerDeleteView.as_view(), name='customer_delete'),
    path('suppliers/', SuppliersListView.as_view(), name='suppliers'),
    path('suppliers/create', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>', SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/update',
         SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete',
         SupplierDeleteView.as_view(), name='supplier_delete'),
]
