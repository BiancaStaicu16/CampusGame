# serializers.py

from rest_framework import serializers

from api import cards
from api.cards.serializers import CardSerializer
from api.gamemode.models import GameMode


class GameModeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMode
        fields = "__all__"


class GameModeCardSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = cards
        fields = '__all__'
