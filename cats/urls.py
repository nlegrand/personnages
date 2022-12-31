from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game:<int:game_id>/', views.game, name='game'),
#    path('/game:<int:game_id>/character:<int:character_id>/', views.character, name='character'),
]
