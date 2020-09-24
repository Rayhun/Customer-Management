from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Customer,Tag,Product,Order


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='pending').count()
    context = {
        'orders':orders,
        'customers':customers,
        # 'total_customers':total_customers,
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
    }

    return render(request, 'accounts/dashbord.html',context)

def products(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'accounts/product.html', context)

def customer(request, pk):
    cusromer = Customer.objects.get(pk=pk)
    return render(request, 'accounts/customer.html')
