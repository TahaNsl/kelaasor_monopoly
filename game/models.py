from django.contrib.auth.models import User
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="players")
    money = models.IntegerField(default=1500)
    position = models.IntegerField(default=0)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} in {self.game.name}"

class Transaction(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="transactions")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="transactions")
    amount = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.user.username} {self.amount} ({self.description})"