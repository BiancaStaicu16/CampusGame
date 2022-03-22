from rest_framework import routers

from api.usercards.viewsets import UserCardViewSet

router = routers.DefaultRouter()
router.register(r"", UserCardViewSet, basename="users_cards")
urlpatterns = router.urls
