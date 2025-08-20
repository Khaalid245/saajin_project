"""
URL configuration for saajin_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import CategoryViewSet, AdminUserViewSet, ArticleViewSet, CommentViewSet
from articles.views_auth import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from articles.admin_views import admin_login, admin_dashboard, admin_articles, admin_categories, admin_comments, home_page,article_detail,about,contact,all_articles

# router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'admin-users', AdminUserViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('saajin-admin/login/', admin_login, name='admin_login'),
    path('saajin-admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('saajin-admin/articles/', admin_articles, name='admin_articles'),
    path('saajin-admin/categories/', admin_categories, name='admin_categories'),
    path('saajin-admin/comments/', admin_comments, name='admin_comments'),

    # Public home page
    path('', home_page, name='home'),
    path('articles/<int:id>/', article_detail, name='article_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('all-articles/', all_articles, name='all_articles'),




]

# 👇 ADD THIS AT THE BOTTOM
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
