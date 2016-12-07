from django.db import models

# Create your models here.
class Pole(models.Model):
    pole = models.IntegerField()
    data_dodania = models.DateTimeField(default=timezone.now)
    data_wydania = models.DateTimeField(null=True)
    ta = models.ForeignKey(TA)

    def __str__(self):
        return str(self.pole)
