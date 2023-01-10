from django.shortcuts import render
from .models import Inventory



def inventorylist(request):
    all_items = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'items': all_items})

