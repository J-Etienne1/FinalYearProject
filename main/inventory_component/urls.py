from django.urls import path
from .import views

urlpatterns = [
    path('', views.InventoryList.as_view(), name="inventory_list"),   
    path('<int:pk>', views.InventoryItemDetail.as_view(), name="item.detail"),   
    path('<int:pk>/edit', views.UpdateItem.as_view(), name="item.update"),   
    path('new', views.CreateItem.as_view(), name="item.new")
]
