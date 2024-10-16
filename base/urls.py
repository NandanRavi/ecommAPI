from django.urls import path
from .views import CustomerListView, ProductListView, OrderListView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='create-customer'),
    path('customers/<int:pk>/', CustomerListView.as_view(), name='update-customer'),
    path('products/', ProductListView.as_view(), name='create-product'),
    path('orders/', OrderListView.as_view(), name='create-order'),
    path('orders/<int:pk>/', OrderListView.as_view(), name='update-order'),
]