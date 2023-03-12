
from datetime import datetime, timedelta, date 
from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect 

from django.urls import reverse 
from django.utils.safestring import mark_safe 
import calendar 

from .models import * 
from .utils import Calendar 
from .forms import BookingForm 

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView



class CalendarView(LoginRequiredMixin,ListView): 
    model = Booking 
    template_name = 'calendar.html' 

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs) 
        d = get_date(self.request.GET.get('month', None)) 
        cal = Calendar(d.year, d.month) 
        # Add the calendar and navigation links 
        html_cal = cal.formatmonth(withyear=True) 
        context['calendar'] = mark_safe(html_cal) 
        context['prev_month'] = prev_month(d) 
        context['next_month'] = next_month(d) 
        return context
    

def get_date(req_month): #get back a requested month from a url or tkae current date
    if req_month: 
        year, month = (int(x) for x in req_month.split('-')) 
        return date(year, month, day=1) 
    return datetime.today() 

def prev_month(d): 
    first = d.replace(day=1) #gets the 1st day of the month
    prev_month = first - timedelta(days=1) 
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month) 
    return month  


def next_month(d): 
    days_in_month = calendar.monthrange(d.year, d.month)[1] 
    last = d.replace(day=days_in_month) 
    next_month = last + timedelta(days=1) 
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month) 
    return month 
 
def booking(request, booking_id=None):
    if booking_id:
        booking = get_object_or_404(Booking, pk=booking_id)
    else:
        booking = Booking()

    if request.method == 'POST':
        if 'delete' in request.POST:
            booking.delete()
            return HttpResponseRedirect(reverse('calendar_component:calendar'))
        else:
            form = BookingForm(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('calendar_component:calendar'))
    else:
        form = BookingForm(instance=booking)

    return render(request, 'booking.html', {'form': form})
