from rest_framework.viewsets import ModelViewSet
from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(ModelViewSet):

    queryset = Publication.objects.all().order_by('-date')
    serializer_class = PublicationSerializer