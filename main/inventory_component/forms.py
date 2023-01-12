

from django import forms
from .models import Inventory




class ItemForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('item', 'description', 'quantity')        
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control my-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-3'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control my-3'})
        }
        # If I want to update the labels for  Item, Description, Quantity
        labels = {
            'item': 'Item Name',
            'description': 'Item Description',
            'quantity': 'Item Quantity'
        }
'''
# USE THIS IF WANT TO ADD SOME ERROR MESSAGE AND CONTROL WHAT WILL BE ACCEPTED IN AN INPUT FIELD I.E TITLE MUST BE iTEM
    def clean_title(self):
        item = self.cleaned_data('item')
        if 'Item name' not in item
            raise forms.validationError('Item must be included the Item field')
        return item

'''