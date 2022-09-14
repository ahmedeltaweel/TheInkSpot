from rest_framework.routers import DefaultRouter

from theinkspot.lists.api.views import ListView

routers = DefaultRouter()
routers.register("", ListView, basename="lists")

app_name = "lists"

urlpatterns = routers.urls
