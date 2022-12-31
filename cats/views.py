from django.shortcuts import render

from .models import Character,Game,Favor

# Create your views here.

def index(request):
    game_list = Game.objects.all()
    context = {
        'game_list': game_list,
        }
    return render(request, 'cats/index.html', context)
def game(request, game_id):
    game = Game.objects.get(pk=game_id)
    character_list = Character.objects.filter(game=game_id)
    context = {
        'character_list': character_list,
        'game': game,
        }
    return render(request, 'cats/game.html', context)
# def charactergame(request, game_id, character_id):
#     character_list = Character.objects()
#     game_list = Game.objects()
#     context = {
#         'character_list': character_list,
#         'game_list': game_list,
#         }
#     return render(request, 'cats/game.html')
    
