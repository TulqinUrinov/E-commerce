from rest_framework.viewsets import ModelViewSet

from data.file.models import File
from data.file.serializers import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

