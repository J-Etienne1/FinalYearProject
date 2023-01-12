from django.shortcuts import render
from .models import Inventory
from django.views.generic import ListView, DetailView, CreateView, UpdateView


from .forms import ItemForm

class InventoryList(ListView):
    model = Inventory
    context_object_name = "items"
    template_name = "inventory_list.html"



class InventoryItemDetail(DetailView):
    model = Inventory
    context_object_name = "item"
    template_name = "inventory_detail.html"




# Used to Create New Inventory Item and add to DB
class CreateItem(CreateView):
    model = Inventory    
    template_name = "inventory_add.html"
    success_url = '/inventory/'
    #fields = ['item', 'description', 'quantity']  #FORM_CLASS REPLACES THIS
    form_class = ItemForm


# Used to Update an Item that is in the Inventory DB
class UpdateItem(UpdateView):
    model = Inventory 
    success_url = '/inventory/' 
    form_class = ItemForm
    context_object_name = "item"
    template_name = "inventory_add.html"