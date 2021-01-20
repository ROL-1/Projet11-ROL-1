from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.


def index(request):
    message = "Bienvenue sur l'application 'user'."
    return HttpResponse(message)


def myaccount(request):
    template = loader.get_template("user/myaccount.html")
    return HttpResponse(template.render(request=request))


# def signup(request):
#     template = loader.get_template("user/signup.html")
#     return HttpResponse(template.render(request=request))


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

