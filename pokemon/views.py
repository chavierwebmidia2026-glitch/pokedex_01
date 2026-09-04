import requests
from django.shortcuts import render


def index(request):
    return render(request, 'pokemon/index.html')


def sobre(request):
    return render(request, 'pokemon/sobre.html')


def pokemons(request):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=20&offset=0'
    response = requests.get(url)
    data = response.json()

    lista_pokemons = []

    for item in data['results']:
        detalhes = requests.get(item['url']).json()

        status_formatado = [
            {'nome': s['stat']['name'], 'valor': s['base_stat']}
            for s in detalhes['stats']
        ]

        lista_pokemons.append({
            'id': detalhes['id'],
            'nome': detalhes['name'],
            'imagem': detalhes['sprites']['other']['official-artwork']['front_default'],
            'tipos': [t['type']['name'] for t in detalhes['types']],
            'altura': f"{detalhes['height'] / 10} m",
            'peso': f"{detalhes['weight'] / 10} kg",
            'habilidades': [a['ability']['name'] for a in detalhes['abilities']],
            'status': status_formatado,
        })

    context = {
        'pokemons': lista_pokemons,
    }

    return render(request, 'pokemon/pokemons.html', context)