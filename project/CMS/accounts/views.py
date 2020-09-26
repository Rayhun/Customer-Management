from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .form import OrderForm
from .filter import OrderFilter



def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='Pending').count()
    order_cancels = orders.filter(statur='Canceled Order').count()
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
        'products': product
    }
    return render(request, 'accounts/product.html', context)

def customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer':customer,
        'orders':orders,
        'orders_count':orders_count,
        'myFilter':myFilter,
    }
    return render(request, 'accounts/customer.html',context)


def createOrder(request, pk): 
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('Product','statur','note'))
    customer = Customer.objects.get(pk=pk)
    formset= OrderFormSet(instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset= OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(pk=pk)
    formset = OrderForm(instance=order)
    if request.method == 'POST':
        formset = OrderForm(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'form':order}
    return render(request, 'accounts/delete.html', context)