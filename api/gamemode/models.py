# models.py

from django.db import models
from api.users.models import User
# from api.cards.models import Card


class GameMode(models.Model):
    """
    Generic timestamp model to be extended by all other models.
    """

    users = models.ManyToManyField(User, on_delete=models.CASCADE)
    # cards = models.ManyToManyField(Card, auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "Game Mode {}".format(self.id)

