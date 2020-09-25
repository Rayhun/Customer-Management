from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .form import OrderForm



def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='Pending').count()
    order_cancels = orders.filter(statur='out for delevery').count()
    context = {
        'orders':orders,
        'customers':customers,
        # 'total_customers':total_customers,
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
        'order_cancels':order_cancels
    }

    return render(request, 'accounts/dashbord.html',context)

def products(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'accounts/product.html', context)

def customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'orders_count':orders_count
    }
    return render(request, 'accounts/customer.html',context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
