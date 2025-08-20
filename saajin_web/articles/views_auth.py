from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny
from .models import AdminUser  # Use custom user model

# Serializer for registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AdminUser  # Use AdminUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = AdminUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# Registration View
class RegisterView(generics.CreateAPIView):
    queryset = AdminUser.objects.all()  # Use AdminUser here too
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
