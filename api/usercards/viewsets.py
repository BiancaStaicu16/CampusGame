from datetime import timedelta
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from api.cards.models import Card
from api.usercards.models import UserCard
from api.usercards.serializers import UserCardSerializer
from rest_framework import viewsets


class UserCardViewSet(viewsets.ModelViewSet):
    """
    UserCards view set for user-card related actions.
    Route: /users_cards/
    """

    queryset = UserCard.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return UserCardSerializer

    @action(detail=False, methods=["POST"], url_path="users_cards")
    def scan_card(self, request):
        requested_user = request.user
        cards_id = 7
        try:
            card = Card.objects.get(card_id=cards_id)
        except:
            return Response({"detail": "Card has not been found."}, status=404)
        if card.value == 0:
            return Response({"detail": "Card value cannot be null."}, status=400)

        user_cards = UserCard.objects.filter(user=requested_user, card=card)
        if user_cards:
            if (
                user_cards.order_by("-created_at").first().created_at
                + timedelta(hours=24)
                > timezone.now()
            ):
                return Response(
                    {"detail": "Cannot scan card more than once in a 24h period."},
                    status=400,
                )

        requested_user.score += card.value
        requested_user.save()
        UserCard.objects.create(user=requested_user, card=card)
        return Response({"detail": "User score has been updated"}, status=200)
