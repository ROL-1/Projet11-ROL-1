from django.db import models
from django.contrib.auth.models import AbstractUser


from django.forms import forms


# class Users(models.Model):
#     first_name_fr = models.CharField(max_length=55)
#     last_name_fr = models.CharField(max_length=55)
#     email = models.EmailField(max_length=254, unique=True)
#     password = forms.CharField(
#         max_length=32, widget=forms.PasswordInput, unique=True
#     )

#     class Meta:
#         unique_together = ("first_name_fr", "last_name_fr")

#     def __str__(self):
#         return self.first_name_fr, " ", self.last_name_fr

#     # password = models.PasswordInput()


class User(AbstractUser):
    pass
