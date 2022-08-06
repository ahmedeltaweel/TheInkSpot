from rest_framework.viewsets import ReadOnlyModelViewSet

from theinkspot.category.api.serializers import CategorySerializer
from theinkspot.category.models import Category


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
