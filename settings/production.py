from . import *

SECRET_KEY = 'jR$x0b]W]?vn<FMN!9K}7p$hE}|'
DEBUG = False
ALLOWED_HOSTS = ['159.89.8.181']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # on utilise l'adaptateur postgresql
        'NAME' : 'purbeurre', # le nom de notre base de données créée précédemment
        'USER': 'rol', # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'mdp123mdp',
        'HOST': '',
        'PORT': '5432',
    }
}

