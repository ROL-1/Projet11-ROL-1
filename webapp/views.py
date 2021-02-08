from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from product.offapi.api_config import CATEGORIES
from product.models import (
    Product,
    Categories,
    Brands,
    NutriscoreGrades,
    CodesProductsOff,
)
from user.models import Favorites

# Create your views here.


def contact(request):
    return render(request, "webapp/contact.html")


def home(request):
    context = {"CATEGORIES": CATEGORIES}
    return render(request, "webapp/home.html", context)


def product(request):
    return render(request, "webapp/product.html")


def legal(request):
    return render(request, "webapp/legal.html")


def results(request):
    # Get user input
    product_id = request.GET["query"]
    # Retrive information from database
    product = Product.objects.get(id=product_id)
    category = product.Categories_id
    nutriscore = product.NutriscoreGrades_id
    results = Product.objects.filter(Categories=category).filter(
        NutriscoreGrades_id__lt=nutriscore
    )
    if not results:  # remplace by get or 404 ?
        # Reaction if no result. # TC template 404
        pass
    else:
        # Reaction if results found
        # Number of products by pages
        paginator = Paginator(results, 6)
        # Get current page number
        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {
            "products": products,
            "product_id": product_id,
            "product": product,
        }
    return render(request, "webapp/results.html", context)


def search(request):
    # Get user input
    query = request.GET["query"]
    # # Reaction if input empty : # TC : BLOQUER ENVOIS FORMULAIRE VIDE, (puis inutile).
    # if not query:
    #     message = "Aucun produit demandé"
    # else:
    # Retrive information from database ("icontains" : case-insensitive)
    results = Product.objects.filter(product_name_fr__icontains=query)
    if not results:
        # If not found, search in "generic_name_fr"
        results = Product.objects.filter(generic_name_fr__icontains=query)
        if not results:  # remplace by get or 404 ?
            # Reaction if no result. # TC template 404
            pass
    else:
        # Reaction if results found
        # Number of products by pages
        paginator = Paginator(results, 6)
        # Get current page number
        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context = {"products": products, "query": query}
    return render(request, "webapp/search.html", context)


# @login_required
def save(request, product_id):
    print("#########################SAVE###########################")
    print("product_id", product_id)
    Favorites.objects.get_or_create(
        Product_id=product_id, CustomUser_id=request.user.id
    )
    print("#########################SAVED###########################")
    return redirect("index")

