from django.conf import settings
from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Character(models.Model):
    type = [('CAT', 'cat'),('HUMAN', 'human'),('BASTET', 'bastet')]
    name = models.CharField(max_length=200)
    age  = models.CharField(max_length=200)
    race = models.CharField(max_length=200)
    line = models.CharField(max_length=200)
    reputation = models.CharField(max_length=200)
    faction = models.CharField(max_length=200)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL)
    game = models.ManyToManyField(Game)
    def __str__(self):
        return self.name
    
class Favor(models.Model):
    character = models.ManyToManyField(Character, blank=True)
    how_many = models.IntegerField()
    title = models.CharField(max_length=50)
    affect = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    warning = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.title

class Advantage(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description

class Flaw(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description
