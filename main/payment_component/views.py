from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings
import stripe
import os



stripe.api_key = settings.STRIPE_SECRET_KEY

#STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')

# need to sort out my Stripe Env Variables so I dont have the secret key on display here
stripe.api_key = 'sk_test_51MaePkDhcRijS6ew9XYy463jjZbdyHiuNnGbQzrTzB7F5GaCSFVbGarnYjoTk5e0A5KCQjr2QDgqrV3LZELovzz3001mHNrZ7X'




class paymentpage(TemplateView):
    template_name = 'paymentpage.html'

class checkout(TemplateView):
    def get(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1Mj6jxDhcRijS6ewdlFEeZsX',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/login/register/',
            #cancel_url='http://localhost:8000', dont need this, will get a warning on HPP if there is an error 
        )
        return redirect(checkout_session.url, code=303)
    
    def post(self, request, *args, **kwargs):
        # Handle POST requests here
        return self.get(request, *args, **kwargs)