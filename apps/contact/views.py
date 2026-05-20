from rest_framework.viewsets import ModelViewSet
from .models import ContactInfo, ContactSubmission
from .serializers import ContactInfoSerializer, ContactSubmissionSerializer


class ContactInfoViewSet(ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class ContactSubmissionViewSet(ModelViewSet):
    queryset = ContactSubmission.objects.all().order_by('-created_at')
    serializer_class = ContactSubmissionSerializer
