from django.contrib import admin

# Register your models here.
from .models import Game, WarhammerCharacter

admin.site.register(Game)
admin.site.register(WarhammerCharacter)

