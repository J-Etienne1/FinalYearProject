
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('inventory/', include('inventory_component.urls'), name="inventory_list"),

    #path('calendar', include('calendar_component.urls')),
    #path('login', include('login_register_component.urls')),
    #path('finance', include('finance_component.urls')),    
    
]
