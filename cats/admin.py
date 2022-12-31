from django.contrib import admin

# Register your models here.
from .models import Favor, Character, Game

admin.site.register(Favor)
admin.site.register(Character)
admin.site.register(Game)
