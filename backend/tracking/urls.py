from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, AddressViewSet, CompanyViewSet, GeoViewSet,
    PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet, TodoViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'geo', GeoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
