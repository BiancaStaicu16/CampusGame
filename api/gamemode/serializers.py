# serializers.py

from rest_framework import serializers

from api.gamemode.models import GameMode


class GameModeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMode
        fields = "__all__"


class GameModePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameMode
        read_only_fields = ["users", "cards"]
        fields = [
            "users",
            "cards"
        ]
