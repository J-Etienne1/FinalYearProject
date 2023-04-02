from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings
import stripe
import os



stripe.api_key = settings.STRIPE_SECRET_KEY

STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')

# Hard coding api key due to issues with api key not been read when set as an environment variable and been read from the setting.py file
stripe.api_key = 'sk_test_51MaePkDhcRijS6ew9XYy463jjZbdyHiuNnGbQzrTzB7F5GaCSFVbGarnYjoTk5e0A5KCQjr2QDgqrV3LZELovzz3001mHNrZ7X'




class paymentpage(TemplateView):
    template_name = 'paymentpage.html'

class checkout(TemplateView):
    def post(self, request, *args, **kwargs):
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1Mj6jxDhcRijS6ewdlFEeZsX',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/login/register/',
            
        )
        return redirect(session.url, code=303)


