from django.urls import path
from .import views

urlpatterns = [
    path('', views.inventorylist.as_view(), name="inventory_list"),   
    path('<int:pk>', views.inventoryitemdetail.as_view(), name="item.detail"),   
    
]
