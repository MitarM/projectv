from django.db import models

# Create your models here.
class Pitanja(models.Model):
    tekst = models.CharField(max_length=200)
    datum = models.DateTimeField()

class Stavka(models.Model):
    pitanje = models.ForeignKey(Pitanja, on_delete=models.CASCADE)
    tekst = models.CharField(max_length=60)
    glasovi = models.IntegerField()