from rest_framework.test import APITestCase

from api.test_utils import test_cards
from api.cards.models import Card

class CardTests(APITestCase):
    def setUp(self) -> None:
        self.url = "/api/cards/"
        self.user = test_cards()

    def test_create_card(self):
        response = self.client.post(
            self.url,
            {
                "title": "Swiop",
                "value": "100",
                "picture": "",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue("Token" in response.data["token"])


def test_CardName(self):
    response = self.client.post(
        self.url,
        {
            "title": "Exeter",
            "value": "100",
            "picture": "",
        },
    )
    self.assertEqual(response.status_code, 201)

