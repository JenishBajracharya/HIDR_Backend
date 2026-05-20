from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-date')
    serializer_class = ProjectSerializer