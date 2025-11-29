from rest_framework import generics, status
from django.contrib.auth import get_user_model
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.serializers import LoginSerializer, UserSerializer

User = get_user_model()


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            refresh['user_id'] = str(user.id)
            refresh['role'] = user.role

            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JWTTokenRefresh(generics.GenericAPIView):
    """
        Refresh JWT token using refresh token.
    """

    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response(
                {'error': 'Refresh Token is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        refresh = RefreshToken(refresh_token)
        access = refresh.access_token
        return Response({
            "access": str(access),
            "refresh": str(refresh)
        }, status=status.HTTP_200_OK)


class MeAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    # permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user

        if user is None or user.is_anonymous:
            raise PermissionDenied("Authentication credentials were not provided.")

        return user
