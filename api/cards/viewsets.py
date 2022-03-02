from rest_framework import viewsets
from rest_framework.response import Response
from api.cards.models import Card
from api.cards.serializers import CardPostSerializer
from rest_framework.decorators import action

from api.users.utils import get_token_response


class CardViewSet(viewsets.ModelViewSet):
    """
    Card view set for card related actions.
    Route: /cards/
    """

    @action(
        detail=False,
        methods=["GET"],
        url_path="display_card",
    )
    def display_card(self):
        """
        Listing all fields from a card
        """
        if self.action == "retrieve":
            return CardPostSerializer



