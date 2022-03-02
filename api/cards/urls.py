from rest_framework import routers

from api.cards.viewsets import CardViewSet

router = routers.DefaultRouter()
router.register(r"", CardViewSet, basename="cards")
urlpatterns = router.urls
