# Serialize Pokemon has HyperlinkedModel
from . import Pokemon
from rest_framework import serializers

class PokemonSerializer (serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pokemon

        fields = ('id', 'name', 'hp', 'type_1', 'type_2',
        'attack', 'defense', 'sp_atk', 'sp_def', 'total',
        'speed')