from rest_framework.test import APITestCase

from api.test_utils import test_user, test_cards
from api.users.models import VerificationCode, User


class UserTests(APITestCase):
    def setUp(self) -> None:
        self.url = "/api/users/"
        self.card = test_cards()
        self.card_1 = test_cards(title="Amory", value=50)
        self.card_2 = test_cards(title="Library", value=20)
        self.card_3 = test_cards(title="Sports Centre", value=150)
        self.user = test_user()
        self.user1 = test_user(
            username="Bob",
            email="bob@exeter.ac.uk",
            name="Bob",
            cards=[self.card_1, self.card_2, self.card_3],
        )
        self.user2 = test_user(
            username="Betty",
            email="betty@exeter.ac.uk",
            name="Betty",
            cards=[self.card_3, self.card_2],
        )

    def test_create_user(self):
        response = self.client.post(
            self.url,
            {
                "username": "maria",
                "email": "maria@exeter.ac.uk",
                "name": "Maria",
                "password": "Orange1!",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue("Token" in response.data["token"])

        # Check you can login after creating account.
        response = self.client.post(
            self.url + "login/",
            {
                "username": "maria@exeter.ac.uk",
                "password": "Orange1!",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_username_optional(self):
        response = self.client.post(
            self.url,
            {
                "email": "maria@exeter.ac.uk",
                "name": "Maria",
                "password": "Orange1!",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_bad_password(self):
        response = self.client.post(
            self.url,
            {
                "username": "maria",
                "email": "maria@example.com",
                "name": "Maria",
                "password": "password",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_name_is_optional(self):
        response = self.client.post(
            self.url,
            {
                "username": "maria",
                "email": "maria@exeter.ac.uk",
                "password": "Orange1!",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_login_and_logout(self):
        # Test user can login.
        response = self.client.post(
            self.url + "login/",
            {
                "username": "marc",
                "password": "Password1",
            },
        )
        self.assertEqual(response.status_code, 200)
        token = response.data["token"]
        self.assertTrue("Token" in token)

        # Test user can logout.
        response = self.client.post(self.url + "logout/", HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_password(self):
        response = self.client.post(
            self.url + "login/",
            {
                "username": "marc",
                "password": "wrong",
            },
        )
        self.assertEqual(response.status_code, 401)

    def test_update_user(self):
        # Login as user and update self.
        self.client.force_authenticate(self.user)
        response = self.client.patch(
            self.url + "me/",
            {
                "name": "New name",
                "password": "C00lPa55",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(id=self.user.id).name, "New name")

        # Logout and login with the new password.
        self.client.logout()
        response = self.client.post(
            self.url + "login/",
            {
                "username": "marc",
                "password": "C00lPa55",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_update_user_cards(self):
        self.client.force_authenticate(self.user)
        response = self.client.patch(self.url + "me/", {"cards": [self.card.id]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(id=self.user.id).cards.count(), 1)

        response = self.client.patch(
            self.url + "me/",
            {
                "cards": [
                    self.card_1.id,
                    self.card_2.id,
                ]
            },
        )
        self.assertEqual(User.objects.get(id=self.user.id).cards.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_user_already_verified(self):
        self.client.force_authenticate(self.user)
        self.user.is_verified = True
        response = self.client.post(self.url + "me/account/request_verification_code/")
        self.assertEqual(response.status_code, 400)

    def test_send_verification_code(self):
        # Request verification code.
        self.client.force_authenticate(self.user)
        response = self.client.post(self.url + "me/account/request_verification_code/")
        self.assertEqual(response.status_code, 200)

        # Try incorrect code.
        response = self.client.post(
            self.url + "me/account/verify/", {"code": "Incorrect Code"}
        )
        self.assertEqual(response.status_code, 401)

        # Check verified with correct code.
        response = self.client.post(
            self.url + "me/account/verify/",
            {"code": VerificationCode.objects.get(id=1).code},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.get(id=self.user.id).is_verified)

    def test_forgot_password_bad_email(self):
        response = self.client.post(
            self.url + "forgot_password/request_verification_code/",
            {"email": "not_a_user@example.com"},
        )
        self.assertEqual(response.status_code, 404)

    def test_forgot_password(self):
        # Request verification code.
        response = self.client.post(
            self.url + "forgot_password/request_verification_code/",
            {"email": self.user.email},
        )
        self.assertEqual(response.status_code, 200)

        # Invalid code.
        response = self.client.post(
            self.url + "forgot_password/verify_code/", {"code": "Incorrect code"}
        )
        self.assertEqual(response.status_code, 401)

        # Verify code is valid.
        response = self.client.post(
            self.url + "forgot_password/verify_code/",
            {"code": VerificationCode.objects.get(id=1).code},
        )
        self.assertEqual(response.status_code, 202)

        # Change password with valid code.
        response = self.client.post(
            self.url + "forgot_password/change_password/",
            {
                "code": VerificationCode.objects.get(id=1).code,
                "password": "N3wPa55w0rd",
            },
        )
        self.assertEqual(response.status_code, 200)

        # Login with new password.
        response = self.client.post(
            self.url + "login/",
            {
                "username": "marc",
                "password": "N3wPa55w0rd",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_get_self_user(self):
        # The user is logged in.
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url + "me/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.user.id)
        self.assertEqual(response.data["password"], self.user.password)

        # Test user has card added.
        self.assertEqual(
            response.data["cards"][0]["id"],
            self.user.cards.first().id,
        )

    def test_soft_delete_user(self):
        response = self.client.post(
            self.url + "login/",
            {
                "username": "marc",
                "password": "Password1",
            },
        )
        response = self.client.delete(
            self.url + "me/", HTTP_AUTHORIZATION=response.data["token"]
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            self.url + "login/",
            {
                "username": "marc",
                "password": "Password1",
            },
        )
        self.assertEqual(response.status_code, 404)

    def test_hard_delete_user(self):
        self.client.force_authenticate(self.user)
        response = self.client.delete(self.url + "me/", {"delete_data": True})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

    def test_leaderboard(self):
        response = self.client.get(self.url + "leaderboard/")
        self.assertEqual(response.status_code, 200)
