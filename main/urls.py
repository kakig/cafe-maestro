from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registrar_usuario", views.registrar_usuario, name="registrar_usuario"),
]
