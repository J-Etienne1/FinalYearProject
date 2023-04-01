from django.forms import ModelForm,TextInput,Textarea
from .models import Inventory

class ItemForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ('item', 'description', 'quantity')
        # set up widgets        
        widgets = {
            'item': TextInput(attrs={'class': 'form-control my-3'}),
            'description': Textarea(attrs={'class': 'form-control my-3'}),
            'quantity': TextInput(attrs={'class': 'form-control my-3'})
        }
        # adding labels so they are displayed when the form is displayed
        labels = {
            'item': 'Item Name',
            'description': 'Item Description',
            'quantity': 'Item Quantity'
        }