
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('inventory/', include('inventory_component.urls'), name="inventory_list"),
    path('login/', include('login_register_component.urls')),
    path('', include('home.urls')),


    #path('calendar', include('calendar_component.urls')),    
    #path('finance', include('finance_component.urls')),   
    
]



