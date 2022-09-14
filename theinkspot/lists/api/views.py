from rest_framework import viewsets

from theinkspot.lists.models import List

from .permissions import ListPermission
from .serializers import ListSerializer


class ListView(viewsets.ModelViewSet, ListPermission):
    serializer_class = ListSerializer
    queryset = List.objects.all()
    permission_classes = [ListPermission]
