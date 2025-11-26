from rest_framework.viewsets import ModelViewSet

from apps.common.pagination import CustomPagination
from apps.file.models import File
from apps.file.serializers import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = CustomPagination
