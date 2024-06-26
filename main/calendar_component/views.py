from .models import Booking 
import calendar 
from django.views.generic import ListView
from .forms import BookingForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import Calendar 
from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponseRedirect 
from datetime import datetime, timedelta, date 
from django.utils.safestring import mark_safe 
from django.urls import reverse 


class CalendarView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'calendar.html'
    login_url = '/login'

    # set up context data for the previous month and next month navgation buttons
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month_navigation = get_date(self.request.GET.get('month', None))
        # creates the calendar 
        cal = Calendar(month_navigation.year, month_navigation.month)

        # make sure a user only see their own bookings
        user_bookings = Booking.objects.filter(user=self.request.user)
        # makes html month calendar that will have a users bookings
        html_cal = cal.formatmonth(withyear=True, bookings=user_bookings)
        # adds calendar to the context data
        context['calendar'] = mark_safe(html_cal)
        # adds previous_month to the context data
        context['previous_month'] = previous_month(month_navigation)
        # adds next_month to the context data
        context['next_month'] = next_month(month_navigation)
        return context


def get_date(current_year_month): # gets the current date and splits it out into year and month that can be used for the previous_month and next_month functions
    if current_year_month: 
        year, month = (int(x) for x in current_year_month.split('-')) 
        return date(year, month, day=1) 
    return datetime.today() 


def previous_month(month_navigation): 
    first_day_in_month = month_navigation.replace(day=1) # makes a new date object for the 1st day of the month
    previous_month = first_day_in_month - timedelta(days=1) # -1 from 1st day of the month to get the last_day_in_month day of the previous month
    month = 'month=' + str(previous_month.year) + '-' + str(previous_month.month) 
    return month  


def next_month(month_navigation): 
    days_in_month = calendar.monthrange(month_navigation.year, month_navigation.month)[1] # get the days in the month
    last_day_in_month = month_navigation.replace(day=days_in_month) # makes a new date object for the last day of the month
    next_month = last_day_in_month + timedelta(days=1) # adds a day to the last day of the month to get the next month
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month) 
    return month 


def booking(request, booking_id=None):
    if booking_id: # checks if there is a bookingid and if there is make sure it is for the user
        booking = get_object_or_404(Booking, pk=booking_id, user=request.user)  
    else:
        booking = Booking() # creates a new booking instance if there is no bookingid

    if request.method == 'POST': # makes sure the booking form is sent using a POST request
        form = BookingForm(request.POST, instance=booking) # adds booking details to the form
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # links the booking with the user
            booking.save()
            return HttpResponseRedirect(reverse('calendar_component:calendar'))
    else:
        form = BookingForm(instance=booking) # if not a POST request form remains and booking is not saved    
    return render(request, 'booking.html', {'form': form}) # displays booking page with the booking form


def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk) # gets booking using bookingid
    booking.delete()
    return redirect('calendar_component:calendar')