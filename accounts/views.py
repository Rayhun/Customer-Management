from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.views.generic import View

# Create your views here.
from .models import *
from .filter import OrderFilter
from .form import OrderForm, CreateUserForm,CustomerForm
from .decorators import unauthenticated_user, allowed_user, admin_only


def registerPage(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            userform = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            qs = User.objects.filter(email=email)
            if qs.exists():
                messages.error(request, 'Email Already Exists')
                return redirect('register')
            else:
                userform.save()
                messages.success(
                    request, username + ' Account create successful'
                )
                return redirect('login')
        context = {
            'form':form
        }
        return render(request, 'accounts/register.html', context) 
    else:
        form = CreateUserForm(request.POST or None)
        context = {
            'form':form
        }
        return render(request, 'accounts/register.html', context) 

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'username or password dos\'t match')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def userProfile(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='Pending').count()
    order_cancels = orders.filter(statur='Canceled Order').count()
    context = {
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
        'order_cancels':order_cancels,
        'orders':orders,
    }
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def accountSetting(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'accounts/account_setting.html', context)

@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    last_five = orders.order_by('-date_created')[0:5]
    customers = Customer.objects.all()
    last_five_customer = customers.order_by('-date_created')[:5]
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='Pending').count()
    order_cancels = orders.filter(statur='Canceled Order').count()
    context = {
        'last_five':last_five,
        'last_five_customer':last_five_customer,
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
        'order_cancels':order_cancels
    }

    return render(request, 'accounts/dashbord.html',context)


@login_required
@admin_only
def all_customer(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='Pending').count()
    order_cancels = orders.filter(statur='Canceled Order').count()
    context = {
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
        'order_cancels':order_cancels,
        'customers':customers
    }
    return render(request, 'accounts/customer_list.html',context)

@login_required
@admin_only
def order_list(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='Pending').count()
    order_cancels = orders.filter(statur='Canceled Order').count()
    context = {
        'orders':orders,
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
        'order_cancels':order_cancels,
    }

    return render(request, 'accounts/order_list.html',context)

@login_required
@admin_only
def order_delivery_list(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_deliver = orders.filter(statur='Delivered')
    order_pending = orders.filter(statur='Pending').count()
    order_cancels = orders.filter(statur='Canceled Order').count()
    context = {
        'order_deliver':order_deliver,
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
        'order_cancels':order_cancels,
    }

    return render(request, 'accounts/order_delivery_list.html',context)

@login_required
@admin_only
def order_pending_list(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='Pending').count()
    order_pendings = orders.filter(statur='Pending')
    order_cancels = orders.filter(statur='Canceled Order').count()
    context = {
        'order_pendings':order_pendings,
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
        'order_cancels':order_cancels,
    }

    return render(request, 'accounts/order_pending_list.html',context)



@login_required
@admin_only
def order_canceled_list(request):
    orders = Order.objects.all()
    total_orders = orders.count()
    order_delivered = orders.filter(statur='Delivered').count()
    order_pending = orders.filter(statur='Pending').count()
    order_cancels = orders.filter(statur='Canceled Order').count()
    order_canceled = orders.filter(statur='Canceled Order')
    context = {
        'order_canceled':order_canceled,
        'total_orders':total_orders,
        'order_delivered':order_delivered,
        'order_pending':order_pending,
        'order_cancels':order_cancels,
    }

    return render(request, 'accounts/order_canceled_list.html',context)


@login_required(login_url='login')
def products(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(request, 'accounts/product.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def createOrder(request, pk): 
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('Product','statur','note','order_content')
    )
    customer = Customer.objects.get(pk=pk)
    formset= OrderFormSet(instance=customer)
    if request.method == 'POST':
        formset= OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def createCustomer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerForm(request.POST or None)
        context = {'form':form}
        return render(request, 'accounts/create_customer.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {
        'form':order,
        }
    return render(request, 'accounts/delete.html', context)

def error_404_view(request, exception):
    return render(request, 'accounts/404.html')