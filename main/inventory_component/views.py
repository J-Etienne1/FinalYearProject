from django.shortcuts import render
from .models import Inventory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .forms import ItemForm
from django.urls import reverse_lazy
class InventoryList(ListView):
    model = Inventory
    context_object_name = "items"
    template_name = "inventory_list.html"



class InventoryItemDetail(DetailView):
    model = Inventory
    context_object_name = "item"
    template_name = "inventory_detail.html"




# Used to CREATE a New Inventory Item and add to DB
class CreateItem(CreateView):
    model = Inventory    
    template_name = "inventory_add.html"
    success_url = '/inventory/'
    #fields = ['item', 'description', 'quantity']  #FORM_CLASS REPLACES THIS
    form_class = ItemForm


# Used to UPDATE an Item that is in the Inventory DB
class UpdateItem(UpdateView):
    model = Inventory 
    success_url = '/inventory/' 
    form_class = ItemForm
    context_object_name = "item"
    template_name = "inventory_add.html"


# Used to DELETE an Item that is in the Inventory DB
class DeleteItem(DeleteView):
    model = Inventory      
    success_url = '/inventory/'
    context_object_name = "item"
    template_name = "inventory_delete.html"

