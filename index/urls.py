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
]
