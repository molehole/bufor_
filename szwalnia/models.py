from django.db import models

# Create your models here.
class Wozek(models.Model):
    wozek = models.IntegerField()
    data_dodania = models.DateTimeField(default=timezone.now)
    data_wydania = models.DateTimeField(null=True)
    ta = models.ForeignKey(TA)
    odebrany = models.BooleanField(default=False)    

    def __str__(self):
        return str(self.wozek)
