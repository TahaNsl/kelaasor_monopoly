from django.db import models

from game.models import Game, Player


class Tile(models.Model):
    TILE_TYPES = [
        ("PROPERTY", "Property"),
        ("STATION", "Station"),
        ("UTILITY", "Utility"),
        ("CHANCE", "Chance"),
        ("CHEST", "Community Chest"),
        ("TAX", "Tax"),
        ("GO", "Go"),
        ("JAIL", "Jail"),
        ("GO_TO_JAIL", "Go to Jail"),
        ("FREE_PARKING", "Free Parking"),
    ]
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="tiles")
    position = models.IntegerField()
    type = models.CharField(max_length=20, choices=TILE_TYPES)

    def __str__(self):
        return f"{self.get_type_display()} ({self.position})"


class Property(models.Model):
    tile = models.OneToOneField(Tile, on_delete=models.CASCADE, related_name="property")
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    rent = models.IntegerField()
    owner = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True, related_name="properties")
    mortgaged = models.BooleanField(default=False)

    def __str__(self):
        return self.name