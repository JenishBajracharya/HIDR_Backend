from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import ContactInfo, ContactSubmission
from .serializers import ContactInfoSerializer, ContactSubmissionSerializer


class ContactInfoViewSet(viewsets.ViewSet):
    def list(self, request):
        contact = ContactInfo.objects.first()

        if not contact:
            return Response({"message": "No contact info found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactInfoSerializer(contact)
        return Response(serializer.data)


class ContactSubmissionViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ContactSubmissionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
