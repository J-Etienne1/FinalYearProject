
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from login_register_component import views


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('inventory/', include('inventory_component.urls'), name="inventory_list"),
    path('login/', include('login_register_component.urls')),    
    path('calendar/', include('calendar_component.urls'), name="calendar"), 
    path('', include('home.urls')),
    #path('', include('login_register_component.urls')),
    #path('home', include('home.urls')),
    
    
    
    
    #path('finance', include('finance_component.urls')),   
    
]



