# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet


# router = DefaultRouter()
# router.register(r'', UserViewSet, basename='accounts')


# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
]