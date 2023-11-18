from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'index'

urlpatterns = [
    # Home
    path('', IndexView.as_view(), name='index'),

    # Customers Urls
    path('customers/', CustomersListView.as_view(), name='customers'),
    path('customers/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/update',
         CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete',
         CustomerDeleteView.as_view(), name='customer_delete'),

    # Suppliers Urls
    path('suppliers/', SuppliersListView.as_view(), name='suppliers'),
    path('suppliers/create', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/<int:pk>/update',
         SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete',
         SupplierDeleteView.as_view(), name='supplier_delete'),

    # Products Urls
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/create', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update',
         ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete',
         ProductDeleteView.as_view(), name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
