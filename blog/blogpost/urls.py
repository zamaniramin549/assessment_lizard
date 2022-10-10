from django.urls import path
from . views import *
urlpatterns = [
   path('', BlogPostView.as_view(), name='blog_post')
]