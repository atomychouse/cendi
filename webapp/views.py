from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(TemplateView):
    template_name = "home.html"

    def get(self, request):
        context = {}
        return render(request, 'webapp/index.html', context)

class Auth(TemplateView):
    template_name = "home.html"

    def post(self, request):
        context = {}
        assert False,request.POST
        return render(request, 'webapp/index.html', context)

class Parent(LoginRequiredMixin,TemplateView):
    login_url = '/'

    def get(self, request):
        context = {}
        assert False,request.POST
        return render(request, 'webapp/index.html', context)