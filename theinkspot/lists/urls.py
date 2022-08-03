 
from django.urls import path
from rest_framework.routers import DefaultRouter
from theinkspot.lists.api.views import ListView
 
routers = DefaultRouter()
routers.register(
    'listview',  ListView, basename='lists')
 
app_name = "lists"

urlpatterns = routers.urls