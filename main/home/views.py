from django.shortcuts import render
from django.http import HttpResponse
# from datetime import datetime
# from django.contrib.auth.decorators import login_required : class based mixis takes care of this
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView




class HomePage(TemplateView):
    template_name = 'home.html'

'''
def home(request):
    return render(request, 'home.html', {'today': datetime.today()})
'''


class AuthorizedViews(LoginRequiredMixin, TemplateView):
    template_name = 'authorized.html'
    login_url = '/admin'



'''
@login_required(login_url = '/admin') #change this to login/reg page when built  and add to each view for each component
def authorized(request):
    return render(request, 'authorized.html', {})
'''