from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.diskusija, name='diskusija'),
    path('kreiranje/', views.kreiranjeDiskusije, name='kreiranjeDiskusije'),
    path('komentar/', views.kreiranjeDiskusije, name='kreiranjeKomentara'),
    # path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
]
