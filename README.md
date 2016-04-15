# Web API REST avec Flask & Swagger

<center>
<u>Python Meetup</u>
</br>
<div style="font-size: 0.9em">Bordeaux &ndash; Node</div>
2016-05-10
</br>
<div style="font-size: 0.8em">Damien Garaud /
<a href="https://twitter.com/jazzydag">@jazzydag</a>
</div>
</center>

---

## Flask

* [Flask](http://flask.pocoo.org/) le micro *framework* Web

* [Flask RESTPlus](https://github.com/noirbizarre/flask-restplus) extension
  Flask pour construire rapidement des API REST

* [Swagger](http://swagger.io/) Interface documentée sur votre API

* [httpie](https://github.com/jkbrzt/httpie) interface en ligne de commande

---

## REST

* Séparation entre le client / interface utilisateur et le stockage des données (serveur)

* Sans état ou *stateless* : toute l'information nécessaire doit être dans la
  requête

* Création / modification / accès à des ressources

* Ressources unitairement identifiée et bien représentées

---

## Mon Usage

* Découpage stockage / consommateur de données

* Accès à des ressources en lecture

* Données calculées : simulation numérique, modèle prédictif
    - prix à date d'une action / d'un produit financier
    - concentrations de polluants à une station de mesure géolocalisée
    - détection de tendance
    - statistiques de l'INSEE à une adresse postale donnée

* Utilisation, amélioration, couche d'abstraction, interfaces Web

---

## Plus loin qu'un Hello World

* Votre collection de musique

* Beets -- http://beets.io/

* Metadata / MusicBrainz

---

## Ressources

REST

How don't hate your APIs
