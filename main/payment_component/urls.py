from django.urls import path
from .import views



urlpatterns = [    
    path('', views.paymentpage.as_view(), name="paymentpage"),
    path('checkout', views.checkout.as_view(), name="checkout"),    
    
]