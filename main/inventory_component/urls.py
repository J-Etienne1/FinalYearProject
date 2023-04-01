from django.urls import path
from .import views

urlpatterns = [
    path('', views.InventoryList.as_view(), name="inventory_list"),       
    path('<int:pk>/edit', views.UpdateItem.as_view(), name="item.update"),   
    path('<int:pk>/delete', views.DeleteItem.as_view(), name="item.delete"),   
    path('new', views.CreateItem.as_view(), name="item.new")
]
