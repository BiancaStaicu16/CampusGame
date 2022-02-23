from rest_framework import routers

from api.users.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r"", UserViewSet, basename="users")
urlpatterns = router.urls
