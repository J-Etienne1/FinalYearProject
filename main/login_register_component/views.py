from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


# use djangos Loginview to handle user login
class Login(LoginView):
    template_name = 'login.html'




# use djangos Logoutview to handle user logout
class Logout(LogoutView):
    template_name = 'logout.html'




# use djangos Createview to handle user registration and UserCreationForm for the registration form
class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    # redirect to login page after registration 
    success_url = 'http://localhost:8000/login/'


