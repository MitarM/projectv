# from django.core.validators import FileExtensionValidator
# validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


# Create your models here.


# class User(AbstractUser):
#     is_organisation = models.BooleanField(default=False)
#     is_volunteer = models.BooleanField(default=False)


class Drzava(models.Model):
    naziv = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.naziv


class Mesto(models.Model):
    naziv = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.naziv


class Ulica(models.Model):
    naziv = models.CharField(max_length=200, null=True)
    naselje = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.naziv + ', ' + self.naselje


class Interesovanje(models.Model):
    naziv = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.naziv


class Organizacija(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    pib = models.IntegerField(unique=True, primary_key=True)
    naziv = models.CharField(max_length=200, null=True)
    opis = models.TextField(max_length=2000, null=True)
    delatnost = models.CharField(max_length=100)
    sajt = models.CharField(max_length=100)
    telefon = models.CharField(max_length=30)
    sediste = models.ForeignKey(Mesto, on_delete=models.CASCADE, default=None)
    ulica = models.ForeignKey(Ulica, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.naziv


DEFAULT_COUNTRY_ID = 1


class Volonter(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # ime = models.CharField(max_length=50, null=True)
    # prezime = models.CharField(max_length=50, null=True)
    datum_rodjenja = models.DateField()
    pol = models.PositiveSmallIntegerField(default=1)
    mesto = models.ForeignKey(Mesto, on_delete=models.CASCADE, default=None)
    ulica = models.ForeignKey(Ulica, on_delete=models.CASCADE, default=None)
    slika = models.ImageField(upload_to='image/', default="images/default.jpg")
    cv = models.FileField(upload_to='cv/', default=None)
    drzavljanstvo = models.ForeignKey(Drzava, on_delete=models.CASCADE, default=DEFAULT_COUNTRY_ID)
    telefon = models.CharField(max_length=30, default=None, blank=True)
    status = models.PositiveSmallIntegerField(default=1)
    # javni_podaci = models.BooleanField(default=False)


    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class DodatniPodaci(models.Model):
    volonter = models.OneToOneField(Volonter, null=True, on_delete=models.CASCADE)
    interesovanja = models.ManyToManyField(Interesovanje)
