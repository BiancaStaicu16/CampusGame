from rest_framework.test import APITestCase
from api.test_utils import test_user, test_cards


class UserCardTests(APITestCase):
    def setUp(self) -> None:
        self.url = "/api/users_cards/"

        # Need user objects
        self.user = test_user()

        # Need card objects
        self.card = test_cards()
        self.card_2 = test_cards(title="Forum", value=100)
        self.card_3 = test_cards(title="Sports Park", value=150)

    def test_scan_card(self):
        response = self.client.post(
            self.url,
            {
                "user": self.user,
                "card": self.card,
            },
        )
        self.assertEqual(response.status_code, 200)
