from django.db import models


class Pizza(models.Model):
    nom = models.CharField(max_length=400)
    ingredients = models.CharField(max_length=800)
    prix = models.IntegerField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):              #Affiche le nom de la classe Pizza @ interface
        return self.nom

    