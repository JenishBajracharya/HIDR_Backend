from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Page
from .serializers import PageSerializer


class PageViewSet(ModelViewSet):

    queryset = Page.objects.all()
    serializer_class = PageSerializer