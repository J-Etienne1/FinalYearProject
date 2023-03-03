from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone
# from django.contrib.auth.decorators import login_required : class based mixis takes care of this
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from calendar_component.models import Booking



class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/login'

    # override the get_context_data method to pass the current date and time to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['events'] = Booking.objects.filter(completed=False)[:2]
        return context
    



class AuthorizedViews(LoginRequiredMixin, TemplateView):
    template_name = 'authorized.html'
    login_url = '/admin'























































'''
@login_required(login_url = '/admin') #change this to login/reg page when built  and add to each view for each component
def authorized(request):
    return render(request, 'authorized.html', {})
'''


'''
This code creates two class-based views for a home page and authorized views using Django's built-in TemplateView and LoginRequiredMixin. The HomePage class is using LoginRequiredMixin to ensure that the user is logged in before they can access the home page. The template_name attribute is used to specify which template to use for the view and the get_context_data method is overridden to pass the current date and time to the template using timezone.now().
'''