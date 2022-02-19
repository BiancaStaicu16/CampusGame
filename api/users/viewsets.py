from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.users.email_manager import (
    email_verification,
    verify_code,
    email_password_reset,
    check_code_is_valid,

)
from api.users.models import User, VerificationCode
from api.users.serializers import (
    UserPostSerializer,
    UserGetSerializer,
)
from api.users.utils import get_token_response


class UserViewSet(viewsets.ModelViewSet):
    """
    User view set for user related actions.
    Route: /users/
    """

    def get_serializer_class(self):
        if self.action == "create":
            return UserPostSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(id=response.data["id"])
        email_verification(user)
        return Response(get_token_response(user), status=201)

    @action(
        detail=False,
        methods=["PATCH", "GET", "DELETE"],
        url_path="me",
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):
        user = request.user

        # Get the currently logged in user data.
        if request.method == "GET":
            serializer = UserGetSerializer(user)
            return Response(serializer.data, status=200)

        # Update the details of the currently logged in user.
        if request.method == "PATCH":
            serializer = UserPostSerializer(user, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors)
            serializer.save()
            return Response({"detail": "User updated."}, status=200)

        #  Set user account is_active to false.
        if request.method == "DELETE":
            if request.data.get("delete_data", False) in ["True", "true", True]:
                user.delete()
            else:
                user.is_active = False
                user.save()
                Token.objects.get(user=user).delete()
            return Response({"detail": "Account deactivated."})

    @action(detail=False, methods=["POST"], url_path="login")
    def login(self, request):
        """
        Login function to authenticate users with either username or email.
        """
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({"detail": "Bad fields."}, status=400)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return Response({"detail": "User does not exist."}, status=404)
        if not user.is_active:
            return Response({"detail": "User account has been deleted."}, status=404)
        if not user.check_password(password):
            return Response({"detail": "Incorrect password."}, status=401)
        return Response(get_token_response(user), status=200)

    @action(
        detail=False,
        methods=["POST"],
        url_path="logout",
        permission_classes=[IsAuthenticated],
    )
    def logout(self, request):
        """
        Logout a logged in user.
        """
        user = request.user
        Token.objects.get(user=user).delete()
        return Response({"detail": "User logged out."}, status=200)

    @action(
        detail=False,
        methods=["POST"],
        url_path="me/account/request_verification_code",
        permission_classes=[IsAuthenticated],
    )
    def request_account_verification_code(self, request):
        """
        Send verification code.
        """
        user = request.user
        if user.is_verified:
            return Response({"detail": "User is already verified."}, status=400)
        try:
            VerificationCode.objects.get(
                user=user, verification_type="account_verification"
            ).delete()
        except VerificationCode.DoesNotExist:
            pass
        email_verification(user)
        return Response({"detail": "Verification email sent."}, status=200)

    @action(
        detail=False,
        methods=["POST"],
        url_path="me/account/verify",
        permission_classes=[IsAuthenticated],
    )
    def verify_code_account(self, request):
        """
        Verify user account given that the verification code is valid.
        """
        user = request.user
        if user.is_verified:
            return Response({"detail": "User is already verified."}, status=400)
        code = request.data.get("code")
        if not code:
            return Response({"detail": "Bad fields."}, status=400)
        try:
            verify_code("account_verification", code)
        except ValueError:
            return Response({"detail": "Code is no longer active."}, status=400)
        except DRFValidationError:
            return Response({"detail": "Code is not correct."}, status=401)
        return Response({"detail": "Email address verified."}, status=200)

    @action(
        detail=False,
        methods=["POST"],
        url_path="forgot_password/request_verification_code",
    )
    def password_reset_email(self, request):
        """
        Sent reset password email.
        """
        email = request.data.get("email")
        if not email:
            return Response({"detail": "Bad fields."}, status=400)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "User does not exist."}, status=404)
        email_password_reset(user)
        return Response({"detail": "Reset password email sent."}, status=200)

    @action(detail=False, methods=["POST"], url_path="forgot_password/verify_code")
    def password_verify_code(self, request):
        """
        Check if verification code for password is valid.
        """
        code = request.data.get("code")
        if not code:
            return Response({"detail": "Bad fields."}, status=400)
        try:
            check_code_is_valid(code, "forgot_password")
        except ValueError:
            return Response({"detail": "Code is no longer active."}, status=400)
        except DRFValidationError:
            return Response({"detail": "Code is not correct."}, status=401)
        return Response({"detail": "Code is valid."}, status=202)

    @action(detail=False, methods=["POST"], url_path="forgot_password/change_password")
    def change_password(self, request):
        """
        Change password given that the code is correct.
        """
        password = request.data.get("password")
        code = request.data.get("code")
        if not password or not code:
            return Response({"detail": "Bad fields."}, status=400)
        try:
            validate_password(password)
        except ValidationError as e:
            raise DRFValidationError(e.messages)
        try:
            verify_code("forgot_password", code, password=password)
        except ValueError:
            return Response({"detail": "Code is no longer active."}, status=400)
        except DRFValidationError:
            return Response({"detail": "Code is not correct."}, status=401)
        return Response({"detail": "Password changed."}, status=200)
