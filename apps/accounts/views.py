from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from .serializers import UserSerializer, RegisterSerializer
from drf_spectacular.utils import extend_schema
from .serializers import RegisterSerializer

class UserViewSet(ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


# class RegisterView(APIView):

#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User created successfully"}, status=201)

#         return Response(serializer.errors, status=400)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .serializers import RegisterSerializer


class RegisterView(APIView):

    @extend_schema(
        request=RegisterSerializer,
        responses={201: RegisterSerializer}
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)