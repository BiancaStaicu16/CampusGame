from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from api.models import TimestampedModel
from api.users.models import User


class Card(TimestampedModel):
    title = models.CharField(max_length=255, unique=True)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    picture = models.FileField(null=True, blank=True)
    # Representing the One-to-Many relationship between users and cards
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Card {}".format(self.title)


class CustomCardManager(BaseUserManager):
    def create_card(self, title, value, **extra_fields):
        """
        Create and save a Card with the given value and
        location name.
        """
        card = self.model(title=title, **extra_fields)
        card.set_title(title)
        card.save()
        return card

    def deal_card(self):
        """When a QR code is scanned, a card will
        be dealt"""
         #TODO

    def view_card(self):
        """Card will appear on screen according to
        the QR code that was scanned"""
        #TODO

    def delete_card(self):
        """Deletes a card"""
        #TODO





