"""Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from account.views import IndexTemplateView
from account.views import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('diskusija/', include('diskutovanje.urls')),
    path('ankete/', include('ankete.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path("", IndexTemplateView.as_view(template_name = "index.html"), name = "index"),
    path("about", TemplateView.as_view(template_name = "about.html"), name = "about"),
    path("login", TemplateView.as_view(template_name = "login.html"), name = "login"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
