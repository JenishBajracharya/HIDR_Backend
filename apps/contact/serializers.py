from rest_framework import serializers

from .models import ContactInfo, ContactSubmission


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ["id", "name", "address", "phone", "email"]


class ContactSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ["id", "full_name", "email", "subject", "message", "submitted_at"]
        read_only_fields = ["id", "submitted_at"]
