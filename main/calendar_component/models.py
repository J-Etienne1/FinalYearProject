from django.db import models 
from django.urls import reverse 
from django.contrib.auth.models import User

class Booking(models.Model): 
    title = models.CharField(max_length=200) 
    details = models.TextField() 
    contact = models.CharField(max_length=200) 
    phone_number = models.CharField(max_length=15)     
    quote = models.DecimalField(max_digits=10, decimal_places=2)     
    materials_needed = models.TextField() 
    materials_cost = models.DecimalField(max_digits=10, decimal_places=2) 
    start_time = models.DateTimeField() 
    end_time = models.DateTimeField() 
    completed = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')    


    @property 
    def get_html_url(self): # creates the a link for each booking on the calendar what when clicked will bring up the booking edit page for the booking clicked 
        url = reverse('calendar_component:booking_edit', args=(self.id,)) 
        return f'<a href="{url}"> {self.title} </a>' 


