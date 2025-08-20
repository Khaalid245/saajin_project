from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, AdminUser, Article, Comment
from .serializers import CategorySerializer, AdminUserSerializer, ArticleSerializer, CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]          # public can read
        return [IsAdminUser()]          # only admin can create/update/delete


class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]  # only admin can CRUD admin users


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']        # ?category=1
    search_fields = ['title', 'content']   # ?search=

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        return [IsAdminUser()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # ❤️ Like endpoint
    @action(methods=['POST'], detail=True, permission_classes=[AllowAny])
    def like(self, request, pk=None):
        article = self.get_object()
        article.likes += 1
        article.save()
        return Response({'likes': article.likes})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
