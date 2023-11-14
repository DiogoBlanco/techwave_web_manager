from django.urls import path
from .views import IndexView, CustomersListView, CustomerDetailView

app_name = 'index'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('customers/', CustomersListView.as_view(), name='customers'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
]
