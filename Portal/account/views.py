from django.shortcuts import render

from diskutovanje.models import Diskusija
from django.views.generic.base import TemplateView

# Create your views here.


class IndexTemplateView(TemplateView):

    def get_context_data(self):
        broj_diskusije = Diskusija.objects.count()
        diskusije = Diskusija.objects.all()
        context = {
            'broj_diskusije': broj_diskusije,
            'diskusije': diskusije,
        }

        return context