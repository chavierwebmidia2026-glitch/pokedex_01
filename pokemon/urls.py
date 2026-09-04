
''' ============================
     < CHWM := CHAVIERWEBMÍDIA >
     < APP URLS.PY := PÁGINA URLS.PY >
     ============================ '''


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pokemons/', views.pokemons, name='pokemons'),
    path('sobre/', views.sobre, name='sobre'),
]