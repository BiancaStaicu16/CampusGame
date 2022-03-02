from rest_framework import viewsets
from rest_framework.response import Response
from api.cards.models import Card
from api.cards.serializers import CardPostSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    User view set for user related actions.
    Route: /cards/
    """

    def display (self, request):
        queryset = Card.fie
        serializer = CardPostSerializer(queryset, many=True)
        return Response(serializer.data)

