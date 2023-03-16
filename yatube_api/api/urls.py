from django.urls import include, path

from api.views import CommentViewSet, GroupViewSet, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("posts", PostViewSet, basename="posts")

router.register("groups", GroupViewSet, basename="groups")

router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path("v1/", include(router.urls)),
]
