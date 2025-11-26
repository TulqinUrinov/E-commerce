from rest_framework.viewsets import ModelViewSet

from apps.common.pagination import CustomPagination
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
