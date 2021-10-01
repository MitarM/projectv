from django.shortcuts import render
from django.http import HttpResponse
from .forms import AnketeCreateForm
from django.shortcuts import redirect
from .forms import KreiranjePitanja
from .models import Anketa
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse("<h1><center><em>Početak ankete naših organizacija</em></center></h1>")

def pitanja(request, id):
    return HttpResponse(f'Pitanje broj: {id}')

@login_required(login_url="../../login")
def kreiranjeAnkete(request):

    form = AnketeCreateForm()
    if (request.method == "POST"):
        form = AnketeCreateForm(request.POST);
    if (form.is_valid()):
        anketa = form.save();
        anketa.autor_ankete = request.user;
        anketa.save();
        return redirect("index");

    context = {
        "form": form
    };

    return render(request, "ankete/kreiranje_ankete.html", context);


def kreiranjePitanja(request):
    id = request.post.get("id")
    form = KreiranjePitanja()
    anketa = Anketa.objects.get(id=id)
    if (form.is_valid()):
        pitanja = form.save();
        pitanja.anketa = anketa
        pitanja.save();
        return redirect("ankete/");

    context = {
        "form": form
    };

    return render(request, "pitanja/kreiranje_pitanja.html", context);