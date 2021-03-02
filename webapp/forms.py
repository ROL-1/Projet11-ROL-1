"""forms for webapp app."""

from django import forms

from dal import autocomplete

from product.models import Product


class ProductForm(forms.ModelForm):
    """Define form form django."""

    class Meta:
        """Meta options."""

        model = Product
        fields = "__all__"  # ("product_name_fr",)
        widgets = {
            "product_name_fr": autocomplete.ModelSelect2(
                url="product-autocomplete"
            )
        }
