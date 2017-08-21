from __future__ import unicode_literals
from ..login_app.models import User
from django.db import models

# Create your models here.
class GoldManager(models.Manager):
    def creategame(self, current_user, gold):
        game = Game.objects.create(user = current_user, gold = gold)
        return game 
class Game(models.Model):
    user = models.ForeignKey(User, related_name= 'games')
    gold = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    objects = GoldManager()
   