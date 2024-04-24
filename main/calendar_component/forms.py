from calendar_component.models import Booking
from django.forms import ModelForm, DateInput, BooleanField


 
class BookingForm(ModelForm):
    completed = BooleanField(required=False) # adding completed to the form
    

    class Meta:
        model = Booking
        exclude = ('user',)  # dont want user to appear on the form
        
        # sets up the start and end time widgets on the form and their format
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'), # displayes the booked start and end times in the widgets
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__' # sets all feilds to the form except whats excluded

    def __init__(self, *args, **kwargs): # when the form is created it will set the date and time
        super(BookingForm, self).__init__(*args, **kwargs)
        # sets the format for start and end times
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',) 
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)