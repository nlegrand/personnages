from django.shortcuts import render

# Create your views here.
def index(request):
    game_list = Game.objects.all()
    context = {
        'game_list': game_list,
        }
    return render(request, 'warhammer1/index.html', context)
def game(request, game_id):
    game = Game.objects.get(pk=game_id)
    character_list = Character.objects.filter(game=game_id)
    context = {
        'character_list': character_list,
        'game': game,
        }
    return render(request, 'warhammer1/game.html', context)
