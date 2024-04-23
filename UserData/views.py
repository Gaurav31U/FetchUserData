from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from .forms import *
from django.contrib.auth.decorators import login_required
from collections import Counter
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import auth

from .models import User


def logouts(request):
    print('logged out')
    logout(request)

    return redirect('index')

#Customer site

def login_user_request(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                if(user.is_customer == False):
                    return render(request, 'SignCustomer.html', {'error_message': 'Your account not registered as Customer'})

                login(request,user)
                return redirect("index")
            else:
                return render(request,'SignCustomer.html',{'error_message':'Your account disable'})
        else:
            return render(request,'SignCustomer.html',{'error_message': 'Invalid Login'})
    return render(request,'SignCustomer.html')
    



def sign_up_user_request(request):
    form =UserSignupForm(request.POST or None)
    if form.is_valid():
        user      = form.save(commit=False)
        username  = form.cleaned_data['username']
        password  = form.cleaned_data['password']
        gender  = form.cleaned_data['gender']
        skill  = form.cleaned_data['skill']

        user.set_password(password)
        user.save()
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return "You're Logged in Successfully"
    
    context ={
        'form':form
    }
    return render(request,'SignCustomer.html',context)
