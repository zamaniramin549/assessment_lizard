from django.urls import path
from . views import *

urlpatterns = [
    path('', loginview, name='login'),
]
