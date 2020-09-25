from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "home"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<int:pk>', views.updateOrder, name="update_order"),
]