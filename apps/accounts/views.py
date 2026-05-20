from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import UserProfile
from .serializers import UserSerializer, RegisterSerializer


class UserViewSet(ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=201)

        return Response(serializer.errors, status=400)