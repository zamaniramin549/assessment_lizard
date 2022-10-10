from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView


class HomeView(TemplateView):
    template_name = 'home/home.html'



class BlogDeatilView(View):
    def get(self, request):
        return render(request, 'home/blog_detail.html')

