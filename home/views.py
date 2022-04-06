from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomerForm, SenderForm
from .models import Customer
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home/home.html')

def delivery(request):
    form = CustomerForm()
    context = {'form':form}
    return render(request,'home/delivery.html', context)

def order(request):
    return render (request, 'home/order.html')

def details(request):
    details = Customer.objects.all()
    
    return render(request, 'home/details.html', 
    {'details': details})

def changedestination(request):
    return render(request, 'home/changedestination.html')

    # return render(request, 'home/details.html')

