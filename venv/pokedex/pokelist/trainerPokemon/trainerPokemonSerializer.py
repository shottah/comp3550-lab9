from . import TrainerPokemon
from rest_framework import serializers
from pokelist.pokemon import PokemonSerializer

# create serializer
# add a new readonly fied to serializer which diplays the id from pokemon model

class TrainerPokemonSerializer(serializers.HyperlinkedModelSerializer):
    poke_stats = PokemonSerializer()
    poke_id = serializers.SerializerMethodField()

    class Meta:
        model = TrainerPokemon
        fields = ('id', 'nickname', 'poke_stats',
        'trainer', 'poke_id')

    def get_poke_id(self, o):
        return o.poke_stats.id