from django.db import models
from bufor import models

# Create your models here.
class Wozek(models.Model):
    wozek = models.IntegerField()
    data_dodania = models.DateTimeField(default=timezone.now)
    data_wydania = models.DateTimeField(null=True)
    ta = models.ForeignKey(TA)
    odebrany = models.BooleanField(default=False)    

    def __str__(self):
        return str(self.wozek)

class Status(models.Model):
    ta = models.ForeignKey(TA)   
    wydany = models.BooleanField(default=False)
    ilosc = models.IntegerField(default=1)
