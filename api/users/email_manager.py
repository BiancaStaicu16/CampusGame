import random
import string

from django.utils import timezone
from rest_framework.exceptions import ValidationError

from djangovue import settings
from api.users.models import VerificationCode

CODE_ACTIVE_MINUTES = 5  # How many minutes a code stays active


def check_code_is_active(verification_code):
    """
    Check if the code is active.
    :param verification_code: VerificationCode instance.
    :return: True if active, False if not.
    """
    return not (
        (timezone.now().timestamp() - verification_code.created_at.timestamp())
        > 60 * CODE_ACTIVE_MINUTES
    )


def generate_code(user, code_type, length):
    """
    Generate a code of random letters and numbers given a length.
    :param user: User instance for whom to generate the code.
    :param code_type: str - one of the options of VerificationType.
    :param length: length of code.
    :return: str - code.
    """
    while True:
        letters_and_digits = string.ascii_letters + string.digits
        result_str = "".join((random.choice(letters_and_digits) for _ in range(length)))
        if not VerificationCode.objects.filter(
            code=result_str
        ).exists():  # In case code already exists.
            VerificationCode.objects.create(
                user=user,
                verification_type=code_type,
                code=result_str,
            )
            return result_str
        else:
            try:  # Attempt to delete code if it exists and is expired.
                v_code = VerificationCode.objects.get(code=result_str)
                if not check_code_is_active(v_code):
                    v_code.delete()
            except:
                pass


def check_code_is_valid(code, code_type):
    """
    Check whether a code is valid.
    :param code: str - code.
    :param code_type: str - one of the options of VerificationType.
    :return: VerificationCode instance.
    :raise: ValidationError - code cannot be validated.
            ValueError - code has expired (also deletes it.
    """
    try:
        v_code = VerificationCode.objects.get(
            verification_type=code_type,
            code=code,
        )
    except:
        raise ValidationError
    if not check_code_is_active(v_code):
        v_code.delete()
        raise ValueError
    return v_code


def verify_code(code_type, code, password=None):
    """
    Verify a code.
    :param code_type: str - one of the options of VerificationType.
    :param code: str - code.
    :param password: (Optional) if code_type is "forgot_password".
    :return: None.
    :raise: Same as 'check_code_is_valid(..)' call.
    """
    v_code = check_code_is_valid(code, code_type)
    if code_type == "account_verification":
        v_code.user.is_verified = True
        v_code.user.save()
    elif code_type == "forgot_password":
        v_code.user.set_password(password)
        v_code.user.save()
    v_code.delete()


def email_verification(user):
    """
    Email verification method.
    :param user: User instance.
    :return: *sends verification email.
    """
    code = generate_code(user, "account_verification", 6)
    # email_subject = "Verify your CampusGame account"
    # html_content = render_to_string("email_templates/email_verify.html", {"code": code})
    # recipient_list = [user.email]
    if not settings.TESTING:
        if settings.DEVELOPMENT:  # Print code in development.
            print("Code: " + code)
        # else:
        # TODO


def email_password_reset(user):
    """
    Email password reset method.
    :param user: User instance.
    :return: *sends password reset email.
    """
    code = generate_code(user, "forgot_password", 6)
    # email_subject = "Reset your CampusGame password"
    # html_content = render_to_string(
    #     "email_templates/password_reset.html", {"user": user, "code": code}
    # )
    # recipient_list = [user.email]
    if not settings.TESTING:
        if settings.DEVELOPMENT:  # Print code in development.
            print("Code: " + code)
        # else:
        # TODO
