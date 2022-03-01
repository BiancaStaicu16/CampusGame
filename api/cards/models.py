from django.db import models
from api.models import TimestampedModel

class Card(TimestampedModel):
    title = models.CharField(max_length=255, unique=True)
    value = models.DecimalField(max_digits=19, decimal_places=2)
    picture = models.FileField(null=True, blank=True)
    code = models.CharField(max_length=255, unique=True,default="000")
    def __str__(self):
        return "Card {}".format(self.title)