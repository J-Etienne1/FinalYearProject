from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Inventory
from .forms import ItemForm



# using the django Listview class of displaying item list
class InventoryList(LoginRequiredMixin, ListView):
    model = Inventory
    context_object_name = "items"
    template_name = "inventory_list.html"
    login_url = '/login'
    # make sure a user only see's there own list of items
    def get_queryset(self):
        return self.request.user.items.all()




# using the django CreateView class to add a new item
class CreateItem(LoginRequiredMixin, CreateView):
    model = Inventory    
    template_name = "inventory_add.html"
    success_url = '/inventory/'
    form_class = ItemForm
    login_url = '/login'
    # makes sure the form is valid and links the created item to the user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



# using the django UpdateView class to update an existing item
class UpdateItem(LoginRequiredMixin, UpdateView):
    model = Inventory 
    success_url = '/inventory/' 
    form_class = ItemForm
    context_object_name = "item"
    template_name = "inventory_add.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()




# using the django DeleteView class to delete an existing item
class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Inventory      
    success_url = '/inventory/'
    context_object_name = "item"
    template_name = "inventory_delete.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()



