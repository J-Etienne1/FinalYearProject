from django.db import models
from django.urls import reverse

'''
class Booking(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    completed = models.BooleanField(default=False)
'''



class Booking(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    contact = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)    
    quote = models.DecimalField(max_digits=5, decimal_places=2)    
    materials_needed = models.TextField()
    materials_cost = models.DecimalField(max_digits=5, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    completed = models.BooleanField(default=False) 
 
 

    @property
    def get_html_url(self):
        url = reverse('calendar_component:event_edit', args=(self.id,))
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