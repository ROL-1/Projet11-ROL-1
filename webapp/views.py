from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from product.offapi.api_config import CATEGORIES
from product.models import (
    Product,
    Categories,
    Brands,
    NutriscoreGrades,
    CodesProductsOff,
)

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


def search(request):
    # Get user input
    query = request.GET["query"]
    # Reaction if input empty : # TC : BLOQUER ENVOIS FORMULAIRE VIDE, (puis inutile).
    if not query:
        message = "Aucun produit demandé"
    else:
        # Retrive information from database ("icontains" : case-insensitive)
        search = Product.objects.filter(product_name_fr__icontains=query)
        if not search:
            # If not found, search in "generic_name_fr"
            search = Product.objects.filter(generic_name_fr__icontains=query)
            if not search:
                # Reaction if no result. # TC template
                message = "Aucun produit trouvé"
        else:
            # Reaction if results finded.
            formatted_results = [
                "<li>{}</li>".format(product.product_name_fr)
                for product in search
            ]
            message = """<ul>{}</ul>""".format("\n".join(formatted_results))
    return HttpResponse(message)
