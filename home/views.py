from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm, SenderForm
from .models import Customer
from django.contrib import messages



def index(request):
    form = CustomerForm()
    context = {'form':form}
    return render(request, 'home/delivery.html', context)

def details(request):
    details = Customer.objects.all()
    return render(request, 'home/details.html', 
    {'details': details})

def changedestination(request):
    return render(request, 'home/changedestination.html')

def home(request):
    context = {'order': order}
    return render(request, 'home/home.html', context)

def delivery(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'update successful!')

    context = {'form':form}
    # context = {'delivery':delivery}
    return render(request, 'home/delivery.html', context)

def Sender(request):
    form = SenderForm()
    context = {'form':form}
    return render(request, 'home/delivery.html', context)


def order(request, pk):
    order = None
    for i in orders:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'home/order.html', context)
