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
    
    
 
 

    @property 
    def get_html_url(self): 
        url = reverse('calendar_component:booking_edit', args=(self.id,)) 
        return f'<a href="{url}"> {self.title} </a>' 













































'''
        title --> title
        details --> description
        quote --> quote
        contact --> contact
        tel --> phone_number
        materials_needed --> materials_needed
        materials_cost --> materials_cost
''' 