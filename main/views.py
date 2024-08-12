from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegistrarUsuarioForm
from .forms import loginForm
from . import models

# Create your views here.


def index(req):
    #return HttpResponse("Hello world")
    return render(req,"main/index.html",)

def registrar_usuario(req):
    if req.method == "POST":
        form = RegistrarUsuarioForm(req.POST)
        if form.is_valid():
            user = models.Usuario(**form.cleaned_data)
            user.save()
        return redirect("login")
    else:
        form = RegistrarUsuarioForm()
    return render(req, "main/registrar_usuario.html", {"form": form})

def login(req):
    if req.method == "GET":
        form = loginForm(req.GET)
        if form.is_valid():
            user = models.Usuario.objects.filter(email=form.cleaned_data["email"]).first()
            if user and user.senha == form.cleaned_data["senha"]:
                return redirect("/") #ir para o painel do usuário
        else:
            form = loginForm()
    return render(req, "main/login.html", {"form": form})
                