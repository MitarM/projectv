from django.db import models

# Create your models here.


class Diskusija(models.Model):
    naziv = models.CharField(max_length=200)
    datum = models.DateTimeField()


class Stavka(models.Model):
    diskusija = models.ForeignKey(Diskusija, on_delete=models.CASCADE)
    tekst = models.CharField(max_length=2000)
    kategorija = 'X'  # ovde treba iz sifarnika uzeti vrednost
    autor = models.CharField(max_length=100)
    mogucnosti = (
        ('1', 'Svi korisnici '),
        ('2', 'Volonteri koji imaju istu oblast interesovanja '),
        ('3', 'Svi volonteri'),
    )
    vidljivost = models.CharField(max_length=1, choices=mogucnosti)