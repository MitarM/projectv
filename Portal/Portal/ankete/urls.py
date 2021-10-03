from django.urls import path
from .views import index
from . import views
from django.views.generic.base import TemplateView

class MyTemplateView(TemplateView):
    pass

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.pitanja, name='pitanja'),
    path("", MyTemplateView.as_view(template_name = "index.html"), name = "index"),
    path("kreiranjeAnkete", views.kreiranjeAnkete, name='kreiranjeAnkete'),
    path('anketa/', views.anketa, name='anketa'),
]




