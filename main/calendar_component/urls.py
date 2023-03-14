
'''     
        DONT NOT EDIT OR DELETE
        IF I CANT RESTRIT VIEWS PER USER JUST USE THIS VERSION
        
'''
from django.urls import path
from .import views


app_name = 'calendar_component'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('booking/new/', views.booking, name='booking_new'),
    path('booking/edit/<int:booking_id>/', views.booking, name='booking_edit'),
  
]



