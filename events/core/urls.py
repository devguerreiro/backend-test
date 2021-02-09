from rest_framework.routers import SimpleRouter

from events.core.views import EventViewSet, InvitationViewSet, UserViewSet

router = SimpleRouter()

router.register("", EventViewSet, basename="event")
router.register("user", UserViewSet, basename="user")
router.register("invitation", InvitationViewSet, basename="invitation")
