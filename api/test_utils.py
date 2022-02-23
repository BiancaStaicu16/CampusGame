from api.users.models import User


def test_user(username="marc", email="marc@example.com", name="Marc", university=None):
    """
    To test an endpoint that requires a user to be authenticated use:
        self.client.force_authenticate(test_user())

    :return: User instance.
    """
    user, created = User.objects.get_or_create(
        username=username,
        email=email,
        name=name,
    )

    if created:
        user.set_password("Password1")
        user.save()
    return user
