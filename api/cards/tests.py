from rest_framework.test import APITestCase
from api.test_utils import test_cards


class CardTests(APITestCase):
    def setUp(self) -> None:
        self.url = "/api/cards/"
        self.card_1 = test_cards()
        self.card_2 = test_cards(title="Amory", value=50)
        self.card_3 = test_cards(title="Library", value=70)

    def test_get_cards(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 3)
