from django.shortcuts import render, redirect
from .models import Organizacija, Volonter

from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationVForm, RegistrationOForm
from .models import User
from django.views.generic.edit import CreateView
from forum.models import Diskusija


# Create your views here.

def index_view(request):
    if request.user.is_authenticated:
        volonteri = Volonter.objects.all()
        organizacije = Organizacija.objects.all()
        diskusije = Diskusija.objects.all()
        # organizacije = Organizacija.objects.filter(company__name=request.user.username)
        context = {
            'organizacije': organizacije,
            'volonteri': volonteri,
            'diskusije': diskusije,

        }

        return render(request, 'index.html', context)

    else:
        # companies = Company.objects.all()
        # context = {
        #     'companies': companies,
        # }
        volonteri = Volonter.objects.all()
        organizacije = Organizacija.objects.all()
        diskusije = Diskusija.objects.all()
        context = {
            'organizacije': organizacije,
            'volonteri': volonteri,
            'diskusije': diskusije,
        }


        return render(request, 'index.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'account/login.html')


# def registerUser(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         Form = UserCreationForm()
#         if request.method == 'POST':
#             Form = UserCreationForm(request.POST)
#             if Form.is_valid():
#                 currUser = Form.save()
#                 Organizacija.objects.create(user=currUser, name=currUser.username)
#                 return redirect('login')
#         context = {
#             'form': Form
#         }
#         return render(request, 'account/register.html', context)


class Registration_vview(CreateView):
    model = User
    form_class = RegistrationVForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'volonter'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class Registration_oview(CreateView):
    model = User
    form_class = RegistrationOForm
    template_name = 'org_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'organizacija'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')



# def applyPage(request):
#     form = ApplyForm()
#     if request.method == 'POST':
#         form = ApplyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context = {'form': form}
#     return render(request, 'apply.html', context)
