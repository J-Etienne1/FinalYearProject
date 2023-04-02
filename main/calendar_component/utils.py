from calendar import HTMLCalendar 


class Calendar(HTMLCalendar): 
	def __init__(self, year=None, month=None): 
		self.year = year 
		self.month = month 
		super(Calendar, self).__init__() 
		
        
	# display a day on the on the calendar and any bookings on a day 
	def formatday(self, day, bookings): 
		bookings_per_day = bookings.filter(start_time__day=day)
		# create a link for booking	
		days_bookings = '' 
		for booking in bookings_per_day: 
			days_bookings += f'<li> {booking.get_html_url} </li>' 

		# show the day and the link for any bookings 
		if day != 0: 
			return f"<td><span class='date'>{day}</span><ul> {days_bookings} </ul></td>" 
		return '<td></td>' 
 



	# formats a week on the on the calendar and any bookings
	def formatweek(self, theweek, bookings): 
		week = '' 
		# add each day of a week and display it
		for d, weekday in theweek: 
			week += self.formatday(d, bookings) 
		return f'<tr> {week} </tr>' 
	


	# formats a month on the on the calendar and any bookings
	def formatmonth(self, withyear=True, bookings=None):
		bookings = bookings.filter(start_time__year=self.year, start_time__month=self.month)


		# table for the calendar
		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n' 
		# month title
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n' 
		# day title
		cal += f'{self.formatweekheader()}\n' 
		# list the weeks in the month and returns a formatted table of days of the week and bookings
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, bookings)}\n' 
		return cal 
 