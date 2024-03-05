from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *

# Create your views here.

class LoginView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'login.html',{'err':err})

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        err = "Invalid credentails!"
        return redirect(f"/accounts/login/?err={err}")
    

class SignupView(View):
    def get(self,request):
        err = request.GET.get("err")
        return render(request,'signup.html',{'err':err})

    def post(self,request):
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password != password2:
            err = "Password not matching"
            return redirect(f"/accounts/signup?err={err}")
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            err = "User with this email or username already exists"
            return redirect(f"/accounts/signup?err={err}")
        
        user = User.objects.create_user(username,email,password)
        # send welcome email
        user.email = email
        user.first_name = full_name
        user.save()

        Account.objects.create(user=user)
        return redirect('/accounts/login')
    
    

class ProfileView(View):
    def get(self,request):
        return render(request,'profile.html',{'user':request.user})
