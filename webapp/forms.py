"""forms for webapp app."""

from django import forms

from dal import autocomplete

from product.models import Product


class ProductForm(forms.ModelForm):
    """Define Product form from django."""

    query = forms.ModelChoiceField(
        label=False,
        queryset=Product.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="product-autocomplete",
            attrs={
                # Set some placeholder
                "data-placeholder": "Recherchez un produit à substituer",
                # Only trigger autocompletion after 1 character has been typed
                "data-minimum-input-length": 1,
            },
        ),
    )

    class Meta:
        """Meta options."""

        model = Product
        fields = ("query",)
