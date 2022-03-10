from api.users.models import User
from api.cards.models import Card
from typing import List, Optional


def test_user(
    username="marc",
    email="marc@example.com",
    name="Marc",
    cards: Optional[List[Card]] = None,
):
    """
    To test an endpoint that requires a user to be authenticated use:
        self.client.force_authenticate(test_user())

    :return: User instance.
    """
    cards = cards or [test_cards()]
    user, created = User.objects.get_or_create(
        username=username,
        email=email,
        name=name,
    )

    if created:
        user.set_password("Password1")
        user.cards.set(cards)
        user.save()
    return user


def test_cards(title: str = "Harrison", value: int = 100) -> Card:
    """Creates a Card object for testing.

    Args:
        title: The card title as a string
        value: The card value as an int

    Returns:
        card: The Card object
    """
    card, _ = Card.objects.get_or_create(
        title=title,
        value=value,
    )
    return card
