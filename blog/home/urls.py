from django.urls import path
from . views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog-detail/', BlogDeatilView.as_view(), name='blog_detail'),
]
