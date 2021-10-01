from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Anketa)
admin.site.register(models.Pitanja)
admin.site.register(models.Stavka)
admin.site.register(models.Otvorena_pitanja)

