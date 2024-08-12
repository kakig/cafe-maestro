from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegistrarUsuarioForm
from . import models

# Create your views here.


def index(req):
    return HttpResponse("Hello world")


def registrar_usuario(req):
    if req.method == "POST":
        form = RegistrarUsuarioForm(req.POST)
        if form.is_valid():
            user = models.Usuario(**form.cleaned_data)
            user.save()
        return redirect("/")
    else:
        form = RegistrarUsuarioForm()
    return render(req, "main/registrar_usuario.html", {"form": form})
