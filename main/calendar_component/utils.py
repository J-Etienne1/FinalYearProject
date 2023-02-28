

from datetime import datetime, timedelta 
from calendar import HTMLCalendar 
from .models import Booking

class Calendar(HTMLCalendar): 
	def __init__(self, year=None, month=None): 
		self.year = year 
		self.month = month 
		super(Calendar, self).__init__() 
		
        
	# formats a day as a table cell that can have a list of bookings for a day	
	def formatday(self, day, events): 
		events_per_day = events.filter(start_time__day=day) # filter events by day
		d = '' 
		for event in events_per_day: 
			d += f'<li> {event.get_html_url} </li>' 

		# If the day is part of the current month, include it in the table cell with the event list
        # Otherwise, return an empty table cell
		if day != 0: 
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>" 
		return '<td></td>' 
 
	# formats a week as a Table row that wil haev table cells for each day
	def formatweek(self, theweek, events): 
		week = '' 
		for d, weekday in theweek: 
			week += self.formatday(d, events) 
		return f'<tr> {week} </tr>' 

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True): 
		events = Booking.objects.filter(start_time__year=self.year, start_time__month=self.month) # pulls the events for a month/year


		# Build the HTML for the calendar table by calling formatweek() for each week in the month
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n' 
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n' 
		cal += f'{self.formatweekheader()}\n' 
		for week in self.monthdays2calendar(self.year, self.month): 
			cal += f'{self.formatweek(week, events)}\n' 
		return cal 
 