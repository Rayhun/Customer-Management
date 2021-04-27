from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

 
urlpatterns = [
    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('user/', views.userProfile, name="user_profile"),
    path('account/', views.accountSetting, name="account"),

    path('', views.home, name = "home"),
    path('all/customer', views.all_customer, name = "customer_list_all"),
    path('all/orders', views.order_list, name = "order_list"),
    path('all/orders/delivery', views.order_delivery_list, name = "order_delivery_list"),
    path('all/orders/pending', views.order_pending_list, name = "order_pending_list"),
    path('all/orders/canceled', views.order_canceled_list, name = "order_canceled"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('create_order/<int:pk>', views.createOrder, name="create_order"),
    path('update_order/<int:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<int:pk>', views.deleteOrder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/passwoer_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name=
         "accounts/password_reset_sent.html"), name="password_reset_done"), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name=
        "accounts/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name=
        "accounts/password_reset_done.html"), name="password_reset_complete"), 
]