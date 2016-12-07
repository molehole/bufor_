from django.db import models

# Create your models here.
class Pole(models.Model):
    pole = models.IntegerField()
    data_dodania = models.DateTimeField(default=timezone.now)
    data_wydania = models.DateTimeField(null=True)
    ta = models.ForeignKey(TA)

    def __str__(self):
        return str(self.pole)


class status(models.Model):
    ta = models.ForeignKey(TA)
    wydany = models.BooleanField(default=False)
    ilosc = models.IntegerField(default=1)

    def __str__(self):
        return str(self.pole)

