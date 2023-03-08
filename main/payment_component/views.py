from django.views.generic import TemplateView
from django.shortcuts import redirect

import stripe
from django.conf import settings



class paymentpage(TemplateView):
    template_name = 'paymentpage.html'


class paymentfailed(TemplateView):
    template_name = 'paymentfailed.html'




    
# need to sort out my Stripe Env Variables so I dont have the secret key on display here
stripe.api_key = 'sk_test_51MaePkDhcRijS6ew9XYy463jjZbdyHiuNnGbQzrTzB7F5GaCSFVbGarnYjoTk5e0A5KCQjr2QDgqrV3LZELovzz3001mHNrZ7X'


'''

Test Card for Successful transaction 
https://stripe.com/docs/testing?testing-method=card-numbers#cards
5454 5454 5454 5454

https://stripe.com/docs/testing#declined-payments
Test Card for Failed transaction 
4000000000000002

'''


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