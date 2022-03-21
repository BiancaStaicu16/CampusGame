from rest_framework import routers

from api.usercards.viewsets import UserCardViewSet
from api.users.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r"", UserViewSet, basename="users")
router.register(r"", UserCardViewSet, basename="users_cards")
urlpatterns = router.urls
