from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

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
