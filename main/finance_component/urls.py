from django.urls import path
from .views import Finance

urlpatterns = [
    path('', Finance.as_view(), name='finance'),
]