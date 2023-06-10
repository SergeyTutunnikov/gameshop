from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.messages import error
from .form import CreateUserForm
from django.urls import reverse_lazy
class LoginPage(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error(request,'Логин или пароль введены неверно')
            return redirect('login')
def sign_out(request):
    logout(request)
    return redirect('login')

class RegisterPage(CreateView):
    model=User
    template_name='register.html'
    form_class=CreateUserForm
    success_url=reverse_lazy('login')