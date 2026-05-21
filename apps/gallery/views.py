# from django.shortcuts import render

# # Create your views here.
# from rest_framework.viewsets import ModelViewSet
# from .models import Image
# from .serializers import ImageSerializer

# class ImageViewSet(ModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer

from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    @extend_schema(
        request=ImageSerializer,
        examples=[
            OpenApiExample(
                "Create Gallery Image",
                value={
                    "image": "(upload a file here)",
                    "caption": "The new book",
                    "category": "network",
                },
                request_only=True,
            )
        ],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)