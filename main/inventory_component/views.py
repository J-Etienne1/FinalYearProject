from django.shortcuts import render
from .models import Inventory
from django.views.generic import ListView, DetailView


class inventorylist(ListView):
    model = Inventory
    context_object_name = "items"
    template_name = "inventory_list.html"

'''
def inventorylist(request):
    all_items = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'items': all_items})
'''



class inventoryitemdetail(DetailView):
    model = Inventory
    context_object_name = "item"
    template_name = "inventory_detail.html"



'''
def inventoryitemdetail(request, pk):
    item = Inventory.objects.get(pk=pk)
    return render(request, 'inventory_detail.html', {'item': item})

'''