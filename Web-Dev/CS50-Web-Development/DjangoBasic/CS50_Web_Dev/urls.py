"""
URL configuration for CS50_Web_Dev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

from FirstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("FirstApp/", include("FirstApp.urls")),
    path('new_year/', include("new_year.urls")),
    path('jack_toDoist/', include("jack_toDoist.urls"))
]
