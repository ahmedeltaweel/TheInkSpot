from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from theinkspot.users.api.views import RegisterUsers, VerifyEmail

from .views import FollowersView, FollowingsView, FollowView, UnFollowView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "api-users"
urlpatterns = router.urls

urlpatterns = [
    path("register/", RegisterUsers.as_view(), name="register"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="access token"),
    path("refresh/token/", jwt_views.TokenRefreshView.as_view(), name="refresh token"),
    path("verify-email/", VerifyEmail.as_view(), name="verify-email"),
    path("followers/<str:username>", FollowersView.as_view(), name="user-followers"),
    path("followings/<str:username>", FollowingsView.as_view(), name="user-following"),
    path("follow/", FollowView.as_view(), name="user-follow"),
    path("unfollow/", UnFollowView.as_view(), name="user-unfollow"),
]
