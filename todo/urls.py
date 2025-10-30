from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView, OrderListCreateAPIView, OrderDetailAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('orders/', OrderListCreateAPIView.as_view()),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view()),
]
