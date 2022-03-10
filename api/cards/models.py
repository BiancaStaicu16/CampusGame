from django.db import models
from api.models import TimestampedModel


class Card(TimestampedModel):
    """
    Fields for Card objects; title is the
    unique identifier
    """

    title = models.CharField(max_length=255, unique=True)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    picture = models.FileField(null=True, blank=True)

    def __str__(self):
        return "Card {}-{}".format(self.title, self.value)
