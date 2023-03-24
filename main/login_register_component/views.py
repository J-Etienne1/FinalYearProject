from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.shortcuts import render



# LOGIN VIEW
class Login(LoginView):
    template_name = 'login.html'




# LOGOUT VIEW  -  # http://127.0.0.1:8000/login/logout
class Logout(LogoutView):
    template_name = 'logout.html'





class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = 'http://localhost:8000/login/'

    # after register get redirected to Login Page, want to maybe put in a page to say acc is registered and now need to log in, will also need to think about STRIPE integration

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('http://localhost:8000/login/')
        return super().get(request, *args, **kwargs)


    

