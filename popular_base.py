from main.models import Insumo

insumos = [
    {"nome": "NPK", "descricao": "Fonte de Nitrogenio, Fosforo, e Potassio ( um adubo generico que tem os 3 nutrientes)", "unidade_medida": "kg"},
    {"nome": "SUPER FOSFOTO SIMPLES", "descricao": "Fonte de fosforo", "unidade_medida": "kg"},
    {"nome": "Ureia", "descricao": "Fonte de nitrogenio", "unidade_medida": "kg"},
    {"nome": "Cloreto de Potássio", "descricao": "Fonte de potássio", "unidade_medida": "kg"},
    {"nome": "Cloreto de benzalcônio", "descricao": "Defensivo agricola", "unidade_medida": "Litro"},
    {"nome": "Permetrina", "descricao": "Defensivo agricola", "unidade_medida": "Litro"},
    {"nome": "Deltametrina", "descricao": "Defensivo agricola", "unidade_medida": "Litro"},
    {"nome": "Espirodiclofeno", "descricao": "Defensivo agricola", "unidade_medida": "Litro"},
    {"nome": "Fenpropatrina", "descricao": "Defensivo agricola", "unidade_medida": "Litro"},
]

for insumo in insumos:
    Insumo(
        nome=insumo["nome"],
        descricao=insumo["descricao"],
        unidade_medida=insumo["unidade_medida"],
    ).save()

from random import randrange
from datetime import timedelta, datetime


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


from main.models import Plantacao
import random

plantacoes = [
    { "nome": "Sabor da Terra", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Águas Claras", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Vereda dos Cafés", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Serra Verde", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Entre Serras", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Santo Antônio", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Vale do Café", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda da Mata", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Água Viva", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Rio Claro", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Sol Nascente", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda das Flores", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Floresta Negra", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Ouro Negro", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Grãos Nobres", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Aroma do Brasil", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Aroma do Cerrado", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Sabor Único", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Delícias da Terra", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Grãos Selecionados", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Elixir dos Deuses", "area_hectares": random.randint(3, 100), "localizacao": "Nomes criativos e memoráveis", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Néctar dos Deuses", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Café com Leite", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
    { "nome": "Alegria em Grãos", "area_hectares": random.randint(3, 100), "localizacao": "Fazenda Terra Mágica", "data_plantio": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)) },
]


for plantacao in plantacoes:
    Plantacao(
        nome=plantacao["nome"],
        area_hectares=plantacao["area_hectares"],
        localizacao=plantacao["localizacao"],
        data_plantio=plantacao["data_plantio"],
    ).save()


from main.models import Plantacao, ProducaoEsperada
import random

plantacoes = Plantacao.objects.all()

producoes = [
    {
        "plantacao": plantacao,
        "quantidade_sacas": random.randint(3, 100),
        "data_previsao": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)),
    }
    for plantacao in plantacoes
]


for producao in producoes:
    ProducaoEsperada(
        plantacao=producao["plantacao"],
        quantidade_sacas=producao["quantidade_sacas"],
        data_previsao=producao["data_previsao"],
    ).save()
