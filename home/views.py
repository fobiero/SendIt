from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm, SenderForm
from .models import Customer
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home/home.html')

# def delivery(request):
#     form = CustomerForm()
#     context = {'form':form}
#     return render(request,'home/delivery.html', context)

# @TODO: Changed code 
def delivery(response):
    if response.method == 'POST':
        form = CustomerForm(response.POST)
        if form.is_valid:
            form.save()
        return redirect("/details")
    else:
        form = CustomerForm()
    return render(response, "home/delivery.html", {"form":form})

# @TODO: Change fetch Customer details 
def details(request):
    details = Customer.objects.all()
    
    return render(request, 'home/details.html', 
    {'details': details})


def order(request):
    return render (request, 'home/order.html')


def changedestination(request):
    pass

    return render(request, 'home/details.html')



