# Project 8, Openclassrooms : Développeur d'application - Python.
<div style="text-align: center">
    <img src="docs/readmeimg.png" style="text-align: center"><br>
</div>
https://openclassrooms.com/fr/paths/68/projects/159/assignment

## Utilisation
A l'aide du champ recherche : vous pouvez chercher un produit dans la base de données.  
Uniquement quelques catégories sont disponibles dans cette version (cf page d'acceuil).  
Une liste de produits pouvant correspondre avec votre recherche sera proposée.  
En choisissant un produit une liste de produits pouvant le substituer, car ayant un meilleur nutriscore, vous sera proposée.  
Vous pouvez également créer un compte pour sauvegarder vos produits favoris.  

## Lien direct vers l'application hébergée sur Heroku
https://lepurbeurre.herokuapp.com/

## Ou : installation et lancement
- Installation :
    * clone
    * `pipenv install`
    * `pipenv shell`
    * `pipenv install -r requirements.txt`

- Installer et peupler la base de données :
    * Créer une base de données, renseigner ses informations de connection dans purbeurre\settings.py  
    ATTENTION : a chaque lancement de cette commande, les données sont effacées.
    * `py manage.py database` (aucun doublon de nom de produit n'est accepté).

- Lancement :
    * `py manage.py runserver`

Le site sera accessible par défaut à l'adresse : 
http://127.0.0.1:8000/

## Deployer sur heroku
Il est nécessaire d'avoir un compte heroku et d'y définir ce projet comme nouveau projet heroku.
Puis passer la commande :
- `git push heroku`

Commande personnalisée pour initialiser la base de données sur heroku :

- (éventuellement pour la réinitialiser : `heroku reset database`)
- `heroku run python manage.py migrate`
- `heroku run bash -a <nom_projet_heroku>`
Depuis le dossier contenant manage.py:
- `python manage.py database`

## Logiciels, librairies, APIs%
- Python 3.8
- Django 3.1
- Ajax (JQuery)
- HTML 5
- CSS 3
- Bootstrap
- PaaS Heroku (WSGI : Gunicorn)
- APIs :
    * OpenFoodfacts
    https://fr.openfoodfacts.org/

## Projet Openclassrooms

### Contexte
La startup Pur Beurre, avec laquelle vous avez déjà travaillé, souhaite développer une plateforme web à destination de ses clients. Ce site permettra à quiconque de trouver un substitut sain à un aliment considéré comme "Trop gras, trop sucré, trop salé".

### Cahier des charges
Le cahier des charges est disponible en cliquant sur ce lien : 
https://company-82435.frontify.com/d/6Yy9WFJdtp8j/pur-beurre-style-guide#/introduction/Notre-identit%C3%A9

### Fonctionnalités
- Affichage du champ de recherche dès la page d’accueil
- La recherche ne doit pas s’effectuer en AJAX
- Interface responsive
- Authentification de l’utilisateur : création de compte en entrant un mail et un mot de passe, sans possibilité de- changer son mot de passe pour le moment.

### Contraintes
- Tests : testez votre projet en adoptant la démarche qui vous semble la plus appropriée (TDD ou tests écrits à la fin- d’une fonctionnalité)
- Utilisez une base de données PostgreSql et non MySQL sous peine de ne pas pouvoir déployer votre application sur Heroku.
- Incluez une page “Mentions Légales” qui contiendra les coordonnées de l’hébergeur ainsi que les auteurs des différentes- ressources libres utilisées (template, photos, icônes, …).
- Suivez les bonnes pratiques de la PEP 8
- Pushez votre code régulièrement sur Github et créez des PR quand vous souhaitez avoir le retour de votre mentor.
- Votre code doit être intégralement écrit en anglais : fonctions, commentaires, …
- Utilisez une méthodologie de projet agile pour travailler en mode projet.
 
### Compétences évaluées
- Mettre en œuvre des tests d’intégration
- Produire un rapport de l’exécution des tests
- Pérenniser son projet web en créant un plan de test
- Développer une application proposant les fonctionnalités attendues par le client
- Mettre en œuvre des tests unitaires

## Lien vers le Trello
https://trello.com/b/aE3Hh6nX/p8-purbeurre