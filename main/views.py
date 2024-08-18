from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegistrarUsuarioForm
from .forms import LoginForm
from . import models

# Create your views here.


def index(req):
    user_obj = models.Usuario.objects.filter(nome="?")
    if len(user_obj) == 0:
        return render(req, "main/index.html", {"user": None})
    return render(req, "main/index.html", {"user": user_obj[0]})


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
    password_error = False
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            user = models.Usuario.objects.filter(
                email=form.cleaned_data["email"]
            ).first()
            if user and user.senha == form.cleaned_data["senha"]:
                return redirect("dashboard")  # ir para o painel do usuário
            else:
                form = LoginForm()
                password_error = True
    else:
        form = LoginForm()
    return render(
        req, "main/login.html", {"form": form, "password_error": password_error}
    )


def dashboard(req):
    insumos = models.Insumo.objects.all()[:10]
    return render(req, "main/dashboard.html", {"insumos": insumos})
