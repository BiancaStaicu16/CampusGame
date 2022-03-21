from django.db import models
from api.users.models import User
from api.cards.models import Card
from api.models import TimestampedModel


class UserCard(TimestampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="card")

   # class Meta:
    #    abstract = False

    def __str__(self):
        return "User Cards {}".format(self.id)
