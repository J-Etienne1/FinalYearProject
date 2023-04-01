from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from calendar_component.models import Booking
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/login' # if user is not logged in and trys to access home.html they are redirected to the login page

    # override the get_context_data method to pass the current date and time to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date_time'] = timezone.now() # gets the current date, year and time
        
        # makes sure a user only sees their own booking and that the 1st two bookings where completed is false are displayed on the homepage
        user_bookings = Booking.objects.filter(completed=False, user=self.request.user)
        context['bookings'] = user_bookings[:2]
        
        return context

    

