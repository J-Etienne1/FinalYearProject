#from django.forms import ModelForm, DateInput
#from calendar_component.models import Booking

from django import forms
from calendar_component.models import Booking

class BookingForm(forms.ModelForm):
    completed = forms.BooleanField(required=False) # adding completed to the form as a bool
    

    class Meta:
        model = Booking
        exclude = ('user',)
        
        # setting up a widget for date/time
        widgets = {
            'start_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': forms.DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__' # making sure all feilds are filled in on the form

    def __init__(self, *args, **kwargs): # when the form is created it will set the date and time
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',) 
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',) 