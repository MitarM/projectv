from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from oglasi.models import Oglas
from .forms import Forma_postavljanja_oglasa
from django.shortcuts import redirect



# class PortalTemplateView(TemplateView):
#     def get_context_data(self):
#         oglasi = Oglas.objects.all()
#         oglasi_javni = Oglas.objects.filter(vidljivost = 1)
#         context = {
#             'oglasi': oglasi,
#             'oglasi_javni': oglasi_javni,
#         }
#         return context

def detaljiOglasa(request, id):

    oglasi = Oglas.objects.get(pk=id)
    context = {
      'oglasi': oglasi
    }
    return render(request, 'oglasi/detail.html', context)

@login_required(login_url="../../login")
def postavljanjeOglasa(request):

    form = Forma_postavljanja_oglasa()
    if (request.method == "POST"):
        form = Forma_postavljanja_oglasa(request.POST)
    if (form.is_valid()):
        oglas = form.save()
        oglas.autor = request.user
        oglas.save()
        return redirect("index")

    context = {
        "form": form
    }

    return render(request, "oglasi/kreiranje_oglasa.html", context)


