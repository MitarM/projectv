from django.urls import path
from . import views

app_name = 'diskutovanje'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detaljiDiskusije, name='detaljiDiskusije'),
]
