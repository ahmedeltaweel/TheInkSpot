import imp
from django.http import Http404
from yaml import serialize
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from theinkspot.lists.models import List
from theinkspot.users.models import User
 
from .serializers import ListSerializer
 
 
 
 
class ListView(viewsets.ModelViewSet, CreateAPIView):
    serializer_class = ListSerializer 
    queryset = List.objects.all()  
    permission_classes = [IsAuthenticated]
 
    def create(self, request):
        user = request.user
        list = request.data 
        username = User.objects.filter(username=user.username).first()
        serializer = self.serializer_class(username, data=list)
        if serializer.is_valid():
            if not list["title"]:
                return Response(
                {"status": "Unacceptable, Lists should have title", "data": serializer.errors}, 
                status=status.HTTP_400_BAD_REQUEST,
            )       
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                 status=status.HTTP_200_OK,
            )
        return Response(
                {"status": "Invalid data", "data": serializer.errors}, 
                status=status.HTTP_400_BAD_REQUEST,
            )    
 
 
    def retrieve(self, request, pk=None):
        user = request.user
        list = get_object_or_404(self.queryset, pk=pk)
        serializer = ListSerializer(list)
        return Response(serializer.data)
 
 
 
    def destroy(self, request, pk=None):
        data = List.objects.get(pk=pk)
        if(data):
            data.delete()
            return Response(
                {"status": "success"},
                 status=status.HTTP_200_OK
            )
 
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )    
 
    def update(self, request, pk=None):
        list = List.objects.get(pk=pk)
        serializer = self.serializer_class(list, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "updated successfully"},
                 status=status.HTTP_200_OK)