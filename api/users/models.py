from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from rest_framework.exceptions import ValidationError

from api.models import TimestampedModel


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class User(TimestampedModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    cards = models.ManyToManyField("cards.Card", blank=True)

    # Permissions fields.
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):
        domain = self.email.split("@")[1]
        if domain != "exeter.ac.uk":
            raise ValidationError("Email must be in format @exeter.ac.uk.")
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return "User {}".format(self.id)


class VerificationCode(TimestampedModel):
    class VerificationType(models.TextChoices):
        ACCOUNT_VERIFICATION = "account_verification"
        FORGOT_PASSWORD = "forgot_password"

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    code = models.CharField(max_length=7)
    verification_type = models.CharField(
        max_length=31, choices=VerificationType.choices
    )
