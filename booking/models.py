from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.db import models

class Maison(models.Model):
    adresse = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='maisons/', blank=True, null=True)

    def __str__(self):
        return self.adresse


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) 
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Reservation(models.Model):
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE) 
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def clean(self):
        if self.date_fin < self.date_debut:
            raise ValidationError("La date de fin doit être postérieure à la date de début.")

    def save(self, *args, **kwargs):  
        self.full_clean() 
        super().save(*args, **kwargs)   



    def __str__(self):
        return f"Réservation de {self.client} pour {self.maison} du {self.date_debut} au {self.date_fin}"
