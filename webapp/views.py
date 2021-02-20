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

# Cleaner
from .cleaner.cleaner import Cleaner

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
    product = Product.objects.get(id=product_id)
    favorite = Favorites.objects.filter(
        Product_id=product_id, CustomUser_id=request.user.id
    ).delete()
    messages.success(
        request, f"Le produit '{product}' a été retiré de vos favoris."
    )
    return redirect("myfavorites")


@login_required
def favorites(request, product_id):
    product = Product.objects.get(id=product_id)
    favorite = Favorites.objects.get_or_create(
        Product_id=product_id, CustomUser_id=request.user.id
    )
    if favorite[1]:
        messages.success(
            request, f"Le produit '{product}' a été ajouté à vos favoris."
        )
    else:
        messages.info(
            request, f"Le produit '{product}' est déjà dans vos favoris."
        )

    return redirect("myfavorites")


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
    results = []
    for favorite in favorites:
        results.append(get_object_or_404(Product, id=favorite.Product_id))
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
    query_cleaned = Cleaner(query).query_cleaned
    print("query_cleaned", query_cleaned)
    try:
        # Retrive information from database ("icontains" : case-insensitive)
        results_lists = []
        for word in query_cleaned:
            results = get_list_or_404(Product, product_name_fr__icontains=word)
            for product in results:
                results_lists.append(product)
            if not results:
                # If not found, search in "generic_name_fr"
                results = get_list_or_404(
                    Product, generic_name_fr__icontains=word
                )
                for product in results:
                    results_lists.append(product)

        # Create pagination from 'results_lists'
        paginator = Paginator(results_lists, 6)
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

