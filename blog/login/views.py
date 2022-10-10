from django.shortcuts import render
from django.views import View
from .forms import LoginForm
# Create your views here.


def loginview(request):
    login_form = LoginForm()
    return render(request, 'login/login.html',{
        'login_form':login_form,
    })

        
