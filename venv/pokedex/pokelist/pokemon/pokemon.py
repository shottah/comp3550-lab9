from django.db import models
from django.db.models import CharField
from django.db.models import IntegerField


# Representation of the base stats of all pokemon based on json dataset
class Pokemon(models.Model):
    name = CharField(max_length=100)
    hp = IntegerField()
    TYPES = (
        ("Normal", "Normal"), 
        ("Fire", "Fire"), 
        ("Water", "Water"), 
        ("Electric", "Electric"), 
        ("Grass", "Grass"), 
        ("Ice", "Ice"),
        ("Fighting", "Fighting"),
        ("Poison", "Poison"), 
        ("Ground", "Ground"), 
        ("Flying", "Flying"), 
        ("Psychic", "Psychic"), 
        ("Bug", "Bug"), 
        ("Ghost", "Ghost"), 
        ("Dragon", "Dragon"), 
        ("Dark", "Dark"), 
        ("Steel", "Steel"), 
        ("Fairy", "Fairy"),
    )
    type_1 = CharField(max_length = 20, choices=TYPES)
    type_2 = CharField(max_length = 20, choices=TYPES, null=True, blank=True)
    attack = IntegerField()
    defense = IntegerField()
    sp_atk = IntegerField()
    sp_def = IntegerField()
    total = IntegerField()
    speed = IntegerField()

    def __str__(self):
        return self.name