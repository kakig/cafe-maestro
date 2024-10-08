from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegistrarUsuarioForm, RegistrarInsumoForm
from .forms import LoginForm
from . import models
from .models import Plantacao, Insumo, ControleInsumo, ProducaoEsperada, ProducaoRealizada, Clima, Trabalhador, ControleTrabalho, Venda


from plotly import express as ex
import pandas as pd

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


""" def dashboard(req):
    insumos = models.Insumo.objects.all()[:10]
    return render(req, "main/dashboard.html", {"insumos": insumos})
 """

def registrar_insumo(req):
    if req.method == "POST":
        form = RegistrarInsumoForm(req.POST)
        if form.is_valid():
            user = models.Insumo(**form.cleaned_data)
            user.save()
            return redirect("dashboard")
        else:
            return render(req, "main/registrar_insumo.html", {"form": form})
    else:
        form = RegistrarInsumoForm()
    return render(req, "main/registrar_insumo.html", {"form": form})

def dashboard(request):
    # Consultando os dados de cada tabela
    plantacoes = Plantacao.objects.all()
    insumos = Insumo.objects.all()
    controles_insumos = ControleInsumo.objects.all()
    producoes_esperadas = ProducaoEsperada.objects.all()
    producoes_realizadas = ProducaoRealizada.objects.all()
    climas = Clima.objects.all()
    trabalhadores = Trabalhador.objects.all()
    controles_trabalhos = ControleTrabalho.objects.all()
    vendas = Venda.objects.all()

    df = pd.DataFrame([{"Plantação": p.plantacao.nome, "Quantidade de Sacas": p.quantidade_sacas, "Data Esperada": p.data_previsao} for p in producoes_esperadas])
    grafico = None
    try:
        fig = ex.bar(df, x="Data Esperada", y="Quantidade de Sacas")
        grafico = fig.to_html(full_html=False)
    except:
        pass

    # Passando os dados para o template
    context = {
        'plantacoes': plantacoes,
        'insumos': insumos,
        'controles_insumos': controles_insumos,
        'producoes_esperadas': producoes_esperadas,
        'producoes_realizadas': producoes_realizadas,
        'climas': climas,
        'trabalhadores': trabalhadores,
        'controles_trabalhos': controles_trabalhos,
        'vendas': vendas,
        'grafico': grafico,
    }
    return render(request, 'main/dashboard.html', context)
