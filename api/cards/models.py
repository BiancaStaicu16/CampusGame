from django.db import models
from api.models import TimestampedModel

class Card(TimestampedModel):
    title = models.CharField(max_length=255, unique=True)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    picture = models.FileField(null=True, blank=True)

    def __str__(self):
        return "Card {}".format(self.title)

class CustomCardManager(BaseUserManager):
    def create_user(self, title, value, **extra_fields):
        """
        Create and save a Card with the given value and
        location name.
        """
        card = self.model(title=title, **extra_fields)
        card.set_title(title)
        card.save()
        return card



class CardName(TimestampedModel):
    card = models.ForeignKey("cards.Card", on_delete=models.CASCADE)




