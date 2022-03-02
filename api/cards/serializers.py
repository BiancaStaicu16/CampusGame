from rest_framework import serializers
from api.cards.models import Card


class CardGetSerializer(serializers.ModelSerializer):
    """
    Converts all fields in the Card model to json data
    """
    class Meta:
        model = Card
        fields = "__all__"
