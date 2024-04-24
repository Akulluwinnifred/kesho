from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'keshoApp/index.html')


def about(request):
    return render(request,'keshoApp/about.html')

def jumper(request):
    return render(request,'keshoApp/jumper.html')

def babes(request):
    return render(request,'keshoApp/babes.html')

def shops(request):
    return render(request,'keshoApp/shops.html')
@login_required
def home(request):
    return render(request,'keshoApp/home.html')

#trying to add a babeform
def AddBabe(request):
    GetBabeform = BabeForm()
    return render(request,'keshoApp/babes.html',{'GetBabeform': GetBabeform})
    # addedbabe = Babe.objects.get(id=pk)
    # babeform = AddBabe(request.POST)
    # if request.method == 'POST':
    #     if babeform.is_valid():
    #         newbabe = babeform.save(commit = False)
    #         newbabe.save()
    # return render(request,'keshoApp/babes.html',{'babeform': babeform,})

def AddPayment(request):
    getpaymentform = AddPaymentForm()
    return render(request,'keshoApp/payment.html',{'getpaymentform':getpaymentform})


