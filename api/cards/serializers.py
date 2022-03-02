from rest_framework import serializers
from api.cards.models import Card


class CardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
