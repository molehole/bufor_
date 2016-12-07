#Modele
from django.db import models
from django.utils import timezone
from datetime import datetime

class Tura(models.Model):
    nr = models.IntegerField()
    data = models.DateField()

    def __str__(self):
        return_string = str(self.nr) + "(" + str(self.data) + ")"
        return str(return_string)

class TA(models.Model):
    tura = models.ForeignKey(Tura)
    nr = models.IntegerField()
    elementy = models.TextField()
    zakonczone = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nr, sefl.zakonczone)

class Etykieta(models.Model):
    ta = models.ForeignKey(TA)
    nr = models.IntegerField()
    pozycja = models.IntegerField(null=True)
    element = models.TextField(null=True)

    def __str__(self):
        return str(self.nr)

class Kolejnosc(models.Model):
    tura = models.TextField()
    data = models.DateField()

    def __str__(self):
        return_string = str(self.tura) + "(" + str(self.data) + ")"
        return return_string
