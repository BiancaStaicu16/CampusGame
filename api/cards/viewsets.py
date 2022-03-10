from rest_framework import viewsets
from api.cards.models import Card
from api.cards.serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    Card view set for card related actions.
    Route: /cards/
    """

    def get_serializer_class(self):
        if self.action == "list":
            return CardSerializer

    def get_queryset(self):
        """
        Used to query card records from the database;
        able to filter by title.
        """
        queryset = Card.objects.all()

        # Filter cards by title.
        title = self.request.GET.get("title")
        if title is not None:
            for term in title.split():
                queryset = queryset.filter(title__icontains=term)

        return queryset
