"""views for user app."""

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# from django.contrib.auth.forms import UserCreationForm
from user.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def myaccount(request):
    """Define view for login."""
    template = loader.get_template("user/myaccount.html")
    return HttpResponse(template.render(request=request))


class SignUpView(generic.CreateView):
    """Define view for sign up."""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

