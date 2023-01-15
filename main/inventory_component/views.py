from django.shortcuts import render
from .models import Inventory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .forms import ItemForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


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
    template_name = "inventory_detail.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()

    



'''
# Used to CREATE a New Inventory Item and add to DB
class CreateItem(LoginRequiredMixin, CreateView):
    model = Inventory    
    template_name = "inventory_add.html"
    success_url = '/inventory/'
    #fields = ['item', 'description', 'quantity']  #FORM_CLASS REPLACES THIS
    form_class = ItemForm
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.items.all()
'''

# Used to CREATE a New Inventory Item and add to DB this is an update of the previous CreateItem as there was a bug when adding a Item when you loggeg back in
class CreateItem(LoginRequiredMixin, CreateView):
    model = Inventory    
    template_name = "inventory_add.html"
    success_url = '/inventory/'
    form_class = ItemForm
    login_url = '/login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)





# Used to UPDATE an Item that is in the Inventory DB
class UpdateItem(LoginRequiredMixin, UpdateView):
    model = Inventory 
    success_url = '/inventory/' 
    form_class = ItemForm
    context_object_name = "item"
    template_name = "inventory_add.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()




# Used to DELETE an Item that is in the Inventory DB
class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Inventory      
    success_url = '/inventory/'
    context_object_name = "item"
    template_name = "inventory_delete.html"
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.items.all()



