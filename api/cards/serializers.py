from rest_framework import serializers
from api.cards.models import Card


class CardSerializer(serializers.ModelSerializer):
    """
    Converts all fields in the Card model to json data
    """

    class Meta:
        model = Card
        read_only_fields = ["id"]
        fields = [
            "id",
            "title",
        ]
