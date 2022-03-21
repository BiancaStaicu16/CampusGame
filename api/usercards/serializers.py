from rest_framework import serializers
from api.usercards.models import UserCard


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        class Meta:
            model = UserCard
            read_only_fields = ["id"]
            fields = [
                "id",
                "card",
                "user",
            ]
