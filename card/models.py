from django.db import models


class Card(models.Model):
    CARD_TYPES = [
        ("CHANCE", "Chance"),
        ("CHEST", "Community Chest"),
    ]
    type = models.CharField(max_length=10, choices=CARD_TYPES)
    description = models.TextField()

    def __str__(self):
        return f"{self.type} - {self.description[:30]}"