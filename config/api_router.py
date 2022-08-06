from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from theinkspot.category.api.views import CategoryViewSet
from theinkspot.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("category", CategoryViewSet, basename="category")

app_name = "api"
urlpatterns = router.urls
