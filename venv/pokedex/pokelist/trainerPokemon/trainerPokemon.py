from django.db import models
from pokelist.models import Pokemon
from pokelist.trainer.trainer import Trainer #uncomment when Trainer Model is created

#create TrainerPokemon model links to pokemon and trainer
# override __str__ method to display nickname

class TrainerPokemon(models.Model):
    nickname = models.CharField(max_length=10)
    poke_stats = models.ForeignKey(Pokemon)
    trainer = models.ForeignKey(Trainer, related_name='party')

    def __str__(self):
        return self.nickname

    class Meta:
        ordering = ('nickname',)