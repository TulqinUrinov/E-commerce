from rest_framework.viewsets import ModelViewSet

from apps.common.pagination import CustomPagination
from apps.user.models import CustomUser
from apps.user.serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = CustomPagination
