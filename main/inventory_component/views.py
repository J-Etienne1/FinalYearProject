from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Inventory
from .forms import ItemForm




class InventoryList(LoginRequiredMixin, ListView):
    model = Inventory
    context_object_name = "items"
    template_name = "inventory_list.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()



class InventoryItemDetail(LoginRequiredMixin, DetailView):
    model = Inventory
    context_object_name = "item"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()

    



class CreateItem(LoginRequiredMixin, CreateView):
    model = Inventory    
    template_name = "inventory_add.html"
    success_url = '/inventory/'
    form_class = ItemForm
    login_url = '/login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class UpdateItem(LoginRequiredMixin, UpdateView):
    model = Inventory 
    success_url = '/inventory/' 
    form_class = ItemForm
    context_object_name = "item"
    template_name = "inventory_add.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()





class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Inventory      
    success_url = '/inventory/'
    context_object_name = "item"
    template_name = "inventory_delete.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()



