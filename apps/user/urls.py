from django.urls import path

from apps.user.views import LoginView, JWTTokenRefresh, MeAPIView, RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='login'),
    path("refresh/", JWTTokenRefresh.as_view(), name='refresh'),
    path("me/", MeAPIView.as_view(), name='me'),
]
