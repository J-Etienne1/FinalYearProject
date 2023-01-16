from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone
# from django.contrib.auth.decorators import login_required : class based mixis takes care of this
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView




class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    

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