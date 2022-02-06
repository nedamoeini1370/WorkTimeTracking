from rest_framework.routers import SimpleRouter

from account.views import UserViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
