from django.urls import path

from .views import ListPosts
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    path("posts/", ListPosts.as_view(), name="posts"),
    path("posts/<int:pk>", ListPosts.as_view(), name="posts-post-put"),
]