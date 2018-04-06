from django.contrib import admin
from .pokemon import Pokemon
# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "type_1", "type_2", "id", "attack", "defense", "speed", "total", "sp_atk", "sp_def")

class TrainerAdmin(admin.ModelAdmin):
    list_display = ()
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Trainer, TrainerAdmin)