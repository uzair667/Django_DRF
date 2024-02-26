from django.urls import path

from .views import fetch_user_data, ListUsers, get_token
from posts.views import fetch_post_data

urlpatterns = [
    path("api_users/", fetch_user_data, name="fetch_user_data"),
    path("api_posts/", fetch_post_data, name="fetch_post_data"),
    path("get_token/", get_token, name="get-token"),
    path("users/", ListUsers.as_view(), name="users"),
    path("users/<int:pk>", ListUsers.as_view(), name="users-post-put"),
]