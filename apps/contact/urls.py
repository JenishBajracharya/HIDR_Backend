from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactInfoViewSet, ContactSubmissionViewSet

router = DefaultRouter()
router.register(r'contact-info', ContactInfoViewSet, basename='contact-info')
router.register(r'contact-submissions', ContactSubmissionViewSet, basename='contact-submissions')

urlpatterns = [
    path('', include(router.urls)),
]
