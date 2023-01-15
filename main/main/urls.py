
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('inventory/', include('inventory_component.urls'), name="inventory_list"),
    path('login/', include('login_register_component.urls')),


    #path('calendar', include('calendar_component.urls')),    
    #path('finance', include('finance_component.urls')),   
    
]
