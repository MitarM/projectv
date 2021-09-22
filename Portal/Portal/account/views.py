from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes

from .models import Organizacija, Volonter

from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationVForm, RegistrationOForm
from .models import User
from django.views.generic.edit import CreateView
from forum.models import Diskusija
from oglasi.models import Oglas
from django.views import View
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from django.urls import reverse


# Create your views here.

def index_view(request):


    if request.user.is_authenticated:
        volonteri = Volonter.objects.all()
        organizacije = Organizacija.objects.all()
        diskusije = Diskusija.objects.all()
        oglasi = Oglas.objects.all()
        context = {
            'organizacije': organizacije,
            'volonteri': volonteri,
            'diskusije': diskusije,
            'oglasi': oglasi
        }


        return render(request, 'index.html', context)

    else:
        volonteri = Volonter.objects.all()
        organizacije = Organizacija.objects.all()
        diskusije = Diskusija.objects.filter(vidljivost=1)
        oglasi = Oglas.objects.filter(vidljivost=1)
        context = {
            'organizacije': organizacije,
            'volonteri': volonteri,
            'diskusije': diskusije,
            'oglasi': oglasi
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




class Registration_vview(CreateView):


    model = User
    form_class = RegistrationVForm
    template_name = 'register.html'

    def get_success_url(self): #Ако је регистација успешна идемо на 'логин' ММ
        return reverse("login")



    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'volonter'
    #     return super().get_context_data(**kwargs)
    #
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('login')

    def post(self, request, *args, **kwargs):

        result = super(Registration_vview, self).post(request, args, kwargs)

        if self.object is not None:
            self.object.is_active = False
            self.object.save()

            currentSite = get_current_site(request)
            userId = self.object.id
            coddedUserId = urlsafe_base64_encode(force_bytes(userId))

            tokenGenerator = PasswordResetTokenGenerator()

            token = tokenGenerator.make_token(self.object)

            context = {
                "user": self.object,
                "domain": currentSite.domain,
                "userId": coddedUserId,
                "token": token
            };

            body = render_to_string("account/email.html", context)

            email = EmailMessage(
                "activation",
                body,
                "admin@email.com",
                [self.object.email]
            )
            email.send()

        return result


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


class ActivationView(View):

    def get(self, request, userId, token):
        user = None
        try:
            id = urlsafe_base64_decode(userId).decode()
            user = User.objects.get(id=id)
        except Exception as error:
            pass

        if (user is None):
            context = {
                "error": "Invalid id."
            }
            return render(request, "error.html", context)

        tokenGenerator = PasswordResetTokenGenerator()

        if not tokenGenerator.check_token(user, token):
            context = {
                "error": "Invalid token."
            };
            return render(request, "error.html", context)

        user.is_active = True
        user.save()

        return redirect("login")

