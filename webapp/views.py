from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def account(request):
    template = loader.get_template("webapp/account.html")
    return HttpResponse(template.render(request=request))


def contact(request):
    template = loader.get_template("webapp/contact.html")
    return HttpResponse(template.render(request=request))


def index(request):
    template = loader.get_template("webapp/index.html")
    return HttpResponse(template.render(request=request))


def product(request):
    template = loader.get_template("webapp/product.html")
    return HttpResponse(template.render(request=request))


def legal(request):
    template = loader.get_template("webapp/legal.html")
    return HttpResponse(template.render(request=request))


def log(request):
    template = loader.get_template("webapp/log.html")
    return HttpResponse(template.render(request=request))


def results(request):
    template = loader.get_template("webapp/results.html")
    return HttpResponse(template.render(request=request))

