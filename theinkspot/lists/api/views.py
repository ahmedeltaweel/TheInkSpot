from rest_framework import viewsets
from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
)

from theinkspot.lists.models import List
from .serializers import ListSerializer


class ListPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

class ListView(viewsets.ModelViewSet, ListPermission):
    serializer_class = ListSerializer
    queryset = List.objects.all()
    permission_classes = [ListPermission]
    