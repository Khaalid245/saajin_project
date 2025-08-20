from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, AdminUserViewSet, ArticleViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'admin-users', AdminUserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
