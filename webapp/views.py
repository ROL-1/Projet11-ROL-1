from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from product.offapi.api_config import CATEGORIES

# Create your views here.


def contact(request):
    template = loader.get_template("webapp/contact.html")
    return HttpResponse(template.render(request=request))


def home(request):
    template = loader.get_template("webapp/home.html")
    context = {"CATEGORIES": CATEGORIES}
    return HttpResponse(template.render(context, request=request))


def product(request):
    template = loader.get_template("webapp/product.html")
    return HttpResponse(template.render(request=request))


def legal(request):
    template = loader.get_template("webapp/legal.html")
    return HttpResponse(template.render(request=request))


def results(request):
    template = loader.get_template("webapp/results.html")
    return HttpResponse(template.render(request=request))

