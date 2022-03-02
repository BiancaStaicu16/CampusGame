from rest_framework import serializers
from api.cards.models import Card


class CardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        read_only_fields = ["title", "value", "picture"]
        fields = [
            "title",
            "value",
            "picture",
        ]
