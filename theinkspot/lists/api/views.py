from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from theinkspot.lists.models import List
from theinkspot.users.models import User

from .serializers import ListSerializer


class ListView(viewsets.ModelViewSet):
    # TODO: check how to maintain ownership of list user
    # permission
    serializer_class = ListSerializer
    queryset = List.objects.all()
    permission_classes = [IsAuthenticated]
