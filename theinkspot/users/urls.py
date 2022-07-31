from django.urls import path

from theinkspot.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from theinkspot.users.api.views import(
    ListCreationView,
    ListDetailsView
 
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    #List URLs 
    path("create/lists/", ListCreationView.as_view(), name="user_list_view" ),
    path("details/lists/<int:pk>/", ListDetailsView.as_view(), name="list_details"),
]
