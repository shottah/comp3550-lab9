from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .pokemon import PokemonTable, Pokemon, PokemonSerializer
from .trainer import Trainer, TrainerSerializer
from .trainerPokemon import TrainerPokemon, TrainerPokemonSerializer

# Create your views here.


def get_pokemon(request):
    pokemon = PokemonTable(Pokemon.objects.all())
    return render(request, 'datatable.html', {
        'pokemon':pokemon
    })


def get_pokemon_range(request, offset, limit):
    offset = int(offset)
    limit = int(limit)
    print(limit)
    pokemon = Pokemon.objects.all()[offset:limit]
    return render(request, 'listing.html', {
        'pokemon':pokemon
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# make ModelViewSets for Pokemon Trainer and TrainerPokemon
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerPokemonViewSet(viewsets.ModelViewSet):
    queryset = TrainerPokemon.objects.all()
    serializer_class = TrainerPokemonSerializer