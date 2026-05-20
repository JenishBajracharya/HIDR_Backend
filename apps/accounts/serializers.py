from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source='userprofile.full_name')
    phone = serializers.CharField(source='userprofile.phone')
    image = serializers.ImageField(source='userprofile.image')

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