# Serialize Trainer
from . import Trainer # uncomment after Trainer model is made
from pokelist.trainerPokemon import TrainerPokemon, TrainerPokemonSerializer
from rest_framework import serializers

class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    party = TrainerPokemonSerializer(many=True, read_only=True)
    party = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='nickname'
    )
    party = serializers.StringRelatedField(many=True)

    class Meta:
        model = Trainerfields = ('id', 'name',
        'num_badges', 'user', 'party')
