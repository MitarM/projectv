from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1><center><em>Početak ankete naših organizacija</em></center></h1>")

def pitanja(request, id):
    return HttpResponse(f'Pitanje broj: {id}')