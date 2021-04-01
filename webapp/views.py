"""views for webapp app."""

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

# Autocomplete
from dal import autocomplete

from .cleaner.cleaner import Cleaner
from .forms import ProductForm
from product.offapi.apiconfig import CATEGORIES
from product.models import (
    Product,
    Categories,
    Brands,
    NutriscoreGrades,
    CodesProductsOff,
)
from user.models import Favorites

# Logging
import logging

logger= logging.getLogger(__name__)
logger.setLevel(logging.INFO)
class ProductAutocomplete(autocomplete.Select2QuerySetView):
    """Autocomplete for Product table."""

    def get_queryset(self):
        """Load product table for autocomplete."""
        if self.q:
            qs = Product.objects.all().order_by("id")
            qs = qs.filter(product_name_fr__icontains=self.q)
        else:
            qs = Product.objects.none()

        return qs



def contact(request):
    """View contact."""
    return render(request, "webapp/contact.html")


@login_required
def delete(request, product_id):
    """View delete, remove user's favorites."""
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
    """View favorites, add a user favorite."""
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
    """View home."""
    context = {"CATEGORIES": CATEGORIES, "form2": ProductForm}
    return render(request, "webapp/home.html", context)


def legal(request):
    """View legal."""
    return render(request, "webapp/legal.html")


@login_required
def myfavorites(request):
    """View myfavorites."""
    try:
        favorites = get_list_or_404(Favorites, CustomUser_id=request.user.id)
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
    except:
        messages.info(request, "Vous n'avez aucun produit sauvegardé.")
    return render(request, "webapp/myfavorites.html")


def product(request, product_id):
    """View product."""
    product = Product.objects.get(id=product_id)
    context = {
        "product": product,
    }
    return render(request, "webapp/product.html", context)


def results(request):
    """View results."""
    # Get user input
    query = request.GET["query"]
    # Retrive information from database
    product = Product.objects.get(id=query)
    category_id = product.Categories_id
    nutriscore_id = product.NutriscoreGrades_id
    try:
        results = get_list_or_404(
            Product,
            Categories=category_id,
            NutriscoreGrades_id__lt=nutriscore_id,
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
    except:
        messages.add_message(
            request,
            messages.INFO,
            "Nous n'avons aucun substitut à vous proposer pour ce produit.",
        )
        context = {
            "product": product,
        }
        return render(request, "webapp/product.html", context)
    return render(request, "webapp/results.html", context)


def search(request):
    """View search."""
    # Get user input
    query = request.GET["query"]
    query_cleaned = Cleaner(query).query_cleaned
    try:
        # Retrive information from database.
        results_lists = []
        # Create list for each word.
        for word in query_cleaned:
            results = get_list_or_404(Product, product_name_fr__contains=word)
            for product in results:
                results_lists.append(product)
            if not results:
                # If not found, search in "generic_name_fr".
                results = get_list_or_404(
                    Product, generic_name_fr__contains=word
                )
                for product in results:
                    results_lists.append(product)

        # Create pagination from 'results_lists'.
        paginator = Paginator(results_lists, 6)
        # Get current page number.
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
            request, messages.INFO, "Aucun produit correspondant trouvé."
        )
        return redirect("home")
    logger.info('New search',exc_info=True)
    return render(request, "webapp/search.html", context)

