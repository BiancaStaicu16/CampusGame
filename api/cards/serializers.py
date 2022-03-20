from rest_framework import serializers
from api.cards.models import Card


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        read_only_fields = ["id"]
        fields = [
            "id",
            "title",
            "value",
        ]
