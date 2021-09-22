from django.contrib.auth.views import LoginView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    # path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path("login/", LoginView.as_view(template_name="account/login.html"), name="login"),
    path('register/', views.Registration_vview.as_view(template_name="account/register.html"), name="register"),
    path('org_register/', views.Registration_oview.as_view(template_name="account/org_register.html"),
         name="org_register"),
    path("activate/<userId>/<token>", views.ActivationView.as_view(), name="activation"),
    
]
