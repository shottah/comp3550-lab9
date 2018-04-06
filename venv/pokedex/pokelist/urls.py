from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'pokemon', views.PokemonViewSet)
router.register(r'trainer', views.TrainerViewSet)
router.register(r'trainer_pkmn', views.TrainerPokemonViewSet)

urlpatterns = [
    url(r'^$', views.get_pokemon, name="poke_table"),
    url(r'^listing/offset/(?P<offset>\d+)/limit/(?P<limit>\d+)/', views.get_pokemon_range, name="poke_list"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
]