from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework import serializers

from api.users.models import User


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ["id", "is_verified"]
        fields = [
            "id",
            "username",
            "email",
            "name",
            "cards",
            "phone_number",
            "password",
            "is_verified",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "required": True},
        }

    def create(self, validated_data):
        if "username" in validated_data:
            if "@" in validated_data["username"]:
                raise DRFValidationError("Username must not contain '@'.")
            if len(validated_data["username"]) < 5:
                raise DRFValidationError("Username must be at least 5 characters long.")
        try:
            validate_password(validated_data["password"])
        except ValidationError as e:
            raise DRFValidationError(e.messages)
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

    def update(self, instance, validated_data):

        instance.name = validated_data.get("name", instance.name)
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.card = validated_data.get("card", instance.card)

        username = validated_data.get("username")
        if username is not None:
            if "@" in validated_data["username"]:
                raise DRFValidationError("Username must not contain '@'.")
            instance.username = username
        email = validated_data.get("email")
        if email is not None:
            instance.email = email
            instance.is_verified = False
        password = validated_data.get("password")
        if password is not None:
            try:
                validate_password(validated_data["password"])
            except ValidationError as e:
                raise DRFValidationError(e.messages)
            instance.set_password(password)
        instance.save()
        return instance
