from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html', {'today': datetime.today()})


@login_required(login_url = '/admin') #change this to login/reg page when built  and add to each view for each component
def authorized(request):
    return render(request, 'authorized.html', {})