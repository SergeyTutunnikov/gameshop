from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.messages import error
from .form import CreateUserForm
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

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
    def form_valid(self,form):
        user=form.instance
        if User.objects.filter(email=user.email).exists():
            form.add_error('email','Данная почта занята')
            return self.form_invalid(form)
        else:
            user.is_active=False
            user.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            subject='Gaming Shop - активация аккаунта'
            template_name='activate_email.html'
            context={
                'email':user.email,
                'username':user.username,
                'protocol':self.request.scheme,
                'domain':get_current_site(self.request).domain,
                'uid':uid,
                'token':token
            }
            body=render_to_string(template_name,context)
            mail=EmailMessage(subject,body,to=[user.email])
            mail.send()
        return super().form_valid(form)
        

def activate_page(request,uidb64,token):
    # try:
        user_id=force_str(urlsafe_base64_decode(uidb64))
        print(user_id)
        print(token)
        user=User.objects.get(pk=user_id)
       
        # if default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return render(request,'activate_email_confirm.html')
        # else:
            # user.delete()
            # return render(request,'activate_error.html')
    # except:
        # return render(request,'activate_error.html')
    
