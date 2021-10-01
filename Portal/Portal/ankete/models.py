from django.db import models
from django.contrib.auth.models import User

class Anketa(models.Model):
    naziv_ankete = models.CharField(max_length=50)
    vidljivost_ankete = models.BooleanField(default=False)
    autor_ankete = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.naziv_ankete

class Pitanja(models.Model):
    pitanje = models.CharField(max_length=200, null=True)
    datum = models.DateTimeField(auto_now_add=True)
    anketa = models.ForeignKey(Anketa, on_delete=models.CASCADE, null=True)
    tip_pitanja = models.BooleanField(default=False)
#   odabir ili otvoreno ili zatvoreno pitanje

skala = (
        (1, "U potunosti se ne slažem"),
        (2, "Delimično se ne slažem"),
        (3, "Niti se slažem, niti se ne slažem"),
        (4, "Delimično se slažem"),
        (5, "U potpunosti se slažem")
        )

class Stavka(models.Model):
    pitanje = models.ForeignKey(Pitanja, on_delete=models.CASCADE, null=True)
    glasovi = models.PositiveSmallIntegerField(default=3, choices=skala)
    ispitanik = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Otvorena_pitanja(models.Model):
    pitanje = models.ForeignKey(Pitanja, on_delete=models.CASCADE, null=True)
    odgovor = models.CharField(max_length=300, null=True)
    ispitanik = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


