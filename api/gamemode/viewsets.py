from rest_framework.decorators import action

from api import users
from api.gamemode.serializers import GameModeCardSerializer

from rest_framework import viewsets
from api.cards.models import Card
from api.cards.serializers import CardSerializer
from api.users.serializers import UserPostSerializer


class GameModeViewSet(viewsets.ModelViewSet):
    """
    Card view set for card related actions.
    Route: /cards/
    """

    def get_serializer_class(self):
        if self.action == "list":
            return CardSerializer

    def get_queryset(self):
        """
        Used to query card records from the
        database and filters records by title.
        """
        queryset = Card.objects.all()

        # Filter cards by title.
        title = self.request.GET.get("title")
        if title is not None:
            for term in title.split():
                queryset = queryset.filter(title__icontains=term)

        return queryset

    # Collect card
    def collect_card(self, request, pk=None):
        # Check if card has been scanned within the last 24 hours (todo)
        user = users.objects.get(pk=pk)
        requested_user = UserPostSerializer(user)
        # call method to add card to user's hand?

    # Get hand total
    @action(detail=False, methods=["GET"], url_path="hand-total")
    def get_hand_total(self, request, pk=None):
        hand_total = 0

        # Collecting users with the given user id
        requested_user = users.objects.get(pk=pk)
        cards = requested_user.GET.get('cards')
        for card in cards:
            serializer = GameModeCardSerializer(card)
            hand_total += serializer.get('value')
        return hand_total

    # Get top 10 users
