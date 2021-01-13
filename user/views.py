from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    message = "Bienvenue sur l'application 'user'."
    return HttpResponse(message)


def myaccount(request):
    template = loader.get_template("user/myaccount.html")
    return HttpResponse(template.render(request=request))
