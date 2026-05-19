from django.urls import path

from .views import ContactInfoViewSet, ContactSubmissionViewSet

urlpatterns = [
    path("info/", ContactInfoViewSet.as_view({"get": "list"}), name="contact-info"),
    path("submit/", ContactSubmissionViewSet.as_view({"post": "create"}), name="contact-submit"),
]
