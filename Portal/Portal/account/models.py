# from django.core.validators import FileExtensionValidator
# validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class User(AbstractUser):
#     is_organisation = models.BooleanField(default=False)
#     is_volunteer = models.BooleanField(default=False)



class Organizacija(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    pib = models.IntegerField(unique=True, primary_key=True)
    naziv = models.CharField(max_length=200, null=True)
    opis = models.TextField(max_length=2000, null=True)
    delatnost = models.CharField(max_length=100)
    sajt = models.CharField(max_length=100)
    telefon = models.CharField(max_length=30)
    sediste = models.CharField(max_length=200, null=True)
    ulica = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.naziv


class Volonter(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # ime = models.CharField(max_length=50, null=True)
    # prezime = models.CharField(max_length=50, null=True)
    datum_rodjenja = models.DateField()
    pol = models.PositiveSmallIntegerField(default=1)
    # mesto = models.CharField(max_length=200, null=True)
    # ulica = models.CharField(max_length=200, null=True)
    slika = models.ImageField(upload_to='image/', default="images/default.jpg")
    cv = models.FileField(upload_to='cv/', default=None)
    # status = models.CharField(max_length=200, null=True)
    # drzavljansto = models.CharField(max_length=200, null=True)
    telefon = models.CharField(max_length=30, default=None, blank=True)


    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
