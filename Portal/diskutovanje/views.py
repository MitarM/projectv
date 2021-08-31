from .models import Diskusija
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    diskusije = Diskusija.objects.all()
    # for diskusija in diskusije:
    #     print(f'{diskusija.naziv}')
    # odgovor = ' , '.join([diskusija.naziv for diskusija in diskusije])
    # return HttpResponse("<h1>INDEX STRANICA</h1>")
    # return HttpResponse(odgovor)
    context = {
        'diskusije': diskusije
    }
    return render(request, 'diskutovanje/index.html', context)

def detaljiDiskusije(request, id):
    diskusije = Diskusija.objects.get(pk=id)
    context = {
        'diskusije': diskusije
    }
    return render(request, 'diskutovanje/detail.html', context)