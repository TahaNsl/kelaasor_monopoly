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


class DiceRoll(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="dice_rolls")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="dice_rolls", null=True, blank=True)

    die1 = models.PositiveSmallIntegerField()
    die2 = models.PositiveSmallIntegerField()

    total = models.PositiveSmallIntegerField(editable=False)
    is_double = models.BooleanField(editable=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        self.total = self.die1 + self.die2
        self.is_double = (self.die1 == self.die2)
        super().save(*args, **kwargs)

    def __str__(self):
        player_repr = self.player.user.username if self.player and self.player.user_id else "—"
        return f"{player_repr} rolled {self.die1},{self.die2} (total={self.total})"


class Transaction(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="transactions")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="transactions")
    amount = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.user.username} {self.amount} ({self.description})"