from django.urls import path
from .import views

'''
WORKDS DO NOT DELETE OR Edit
app_name = 'calendar_component'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
  
]

'''



app_name = 'calendar_component'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
  
]