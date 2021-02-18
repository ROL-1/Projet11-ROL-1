from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import loader
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    redirect,
    render,
)

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

# Autocomplete

from dal import autocomplete

from product.models import Product

from .forms import ProductForm


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.request.user.is_authenticated():
        #     return Product.objects.none()

        if self.q:
            qs = Product.objects.all()
            qs = qs.filter(product_name_fr__icontains=self.q)
        else:
            qs = Product.objects.none()

        return qs


# DANGER !!! As you might have noticed, we have just exposed data through a public URL.
# Please don’t forget to do proper permission checks in get_queryset. !!!


def contact(request):
    return render(request, "webapp/contact.html")


@login_required
def delete(request, product_id):
    print("#########################ERASE###########################")
    print("product_id", product_id)
    Favorites.objects.filter(
        Product_id=product_id, CustomUser_id=request.user.id
    ).delete()
    print("#########################ERASED###########################")
    return redirect("myfavorites")


@login_required
def favorites(request, product_id):
    print("#########################SAVE###########################")
    print("product_id", product_id)
    Favorites.objects.get_or_create(
        Product_id=product_id, CustomUser_id=request.user.id
    )
    print("#########################SAVED###########################")
    return redirect("results")


def home(request):
    context = {
        "CATEGORIES": CATEGORIES,
    }
    return render(request, "webapp/home.html", context)


def legal(request):
    return render(request, "webapp/legal.html")


@login_required
def myfavorites(request):
    favorites = get_list_or_404(Favorites)
    print(favorites)
    results = []
    for favorite in favorites:
        results.append(get_object_or_404(Product, id=favorite.Product_id))
    print(results)
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
    }
    return render(request, "webapp/myfavorites.html", context)


def product(request):
    product_id = request.GET["query"]
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(request, "webapp/product.html", context)


def results(request):
    # Get user input
    query = request.GET["query"]
    # Retrive information from database
    product = Product.objects.get(id=query)
    category = product.Categories_id
    nutriscore = product.NutriscoreGrades_id
    results = get_list_or_404(
        Product, Categories=category, NutriscoreGrades_id__lt=nutriscore
    )
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
        "product_id": query,
        "product": product,
        "query": query,
    }
    return render(request, "webapp/results.html", context)


def search(request):
    # Get user input
    query = request.GET["query"]
    try:
        # Retrive information from database ("icontains" : case-insensitive)
        results = get_list_or_404(Product, product_name_fr__icontains=query)
        if not results:
            # If not found, search in "generic_name_fr"
            results = get_list_or_404(
                Product, generic_name_fr__icontains=query
            )
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
    except:
        messages.add_message(
            request, messages.ERROR, "Aucun produit correspondant trouvé."
        )
        return redirect("home")
    return render(request, "webapp/search.html", context)

