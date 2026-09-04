
''' ============================
     < CHWM := CHAVIERWEBMÍDIA >
     < VIEWS := PÁGINA VIEWS.PY >
     ============================ '''

import requests
from django.shortcuts import render


def index(request):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=20&offset=0'
    response = requests.get(url)
    data = response.json()

    pokemons = []

    for item in data['results']:
        detalhes = requests.get(item['url']).json()

        pokemons.append({
            'id': detalhes['id'],
            'nome': detalhes['name'],
            'imagem': detalhes['sprites']['other']['official-artwork']['front_default'],
            'tipos': [t['type']['name'] for t in detalhes['types']],
        })

    context = {
        'pokemons': pokemons,
    }

    return render(request, 'pokemon/index.html', context)