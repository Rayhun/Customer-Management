from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

    path('', views.home, name = "home"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>', views.customer, name="customer"),
    path('create_order/<int:pk>', views.createOrder, name="create_order"),
    path('update_order/<int:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<int:pk>', views.deleteOrder, name="delete_order"),
]