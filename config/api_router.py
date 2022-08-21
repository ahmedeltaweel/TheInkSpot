from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "api"
urlpatterns = router.urls

urlpatterns += [

    path("api/users/", include("theinkspot.users.api.urls")),
]
