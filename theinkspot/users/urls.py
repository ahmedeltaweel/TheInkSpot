from django.urls import path

from theinkspot.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

from theinkspot.users.api.views import(
    user_list_view,
    user_list_details_view,
 )


app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    #List URLs 
    path('lists/', view=user_list_view, name="user_list_view" ),
    path('lists/<int:pk>/', view=user_list_details_view, name="list_details"),
]
