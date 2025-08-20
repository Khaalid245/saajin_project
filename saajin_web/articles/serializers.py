from rest_framework import serializers
from .models import Category, AdminUser, Article, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = AdminUser
        fields = ['id', 'username', 'email', 'password', 'is_staff']

    def create(self, validated_data):
        user = AdminUser(
            username=validated_data['username'],
            email=validated_data['email'],
            is_staff=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'image', 'created_at',
                  'category', 'category_id', 'likes']   # 🟣 include likes


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), source='article', write_only=True
    )
    class Meta:
        model = Comment
        fields = ['id', 'article', 'article_id', 'name', 'email', 'message', 'created_at']
