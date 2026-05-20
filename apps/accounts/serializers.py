from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone', 'image']


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source='profile.full_name', read_only=True)
    phone = serializers.CharField(source='profile.phone', read_only=True)
    image = serializers.ImageField(source='profile.image', read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'full_name',
            'phone',
            'image',
        ]


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'full_name', 'phone', 'image']

    def create(self, validated_data):

        full_name = validated_data.pop('full_name')
        phone = validated_data.pop('phone')
        image = validated_data.pop('image', None)

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        UserProfile.objects.create(
            user=user,
            full_name=full_name,
            phone=phone,
            image=image
        )

        return user