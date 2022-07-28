from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import UserSerializer, ListSerializer
from theinkspot.users.models import List
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)



class ListCreationView(APIView):
    #serializer_class = ListView

    def post(self, request):
        list = request.data
        serializer = self.serializer_class(data=list)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
     
user_list_view = ListCreationView.as_view()

class ListDetailsView(APIView):
    def retrieve(self, request, pk): # adding primary key
       # queryset = List.objects.all()
       # list = get_object_or_404(queryset, pk=pk)
        try:
            list = List.objects.get(pk=pk)
        except List.DoesNotExist:
             raise Http404("Not exist.")

        serializer = ListSerializer(list)
        return Response(serializer.data)
        
user_list_details_view = ListDetailsView.as_view()



# @api_view(['GET', 'POST'])
# def list_create(request):

#     if request.method == 'GET':
#         lists = List.objects.all()
#         serializer = ListSerializer(lists, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE'])
# def list_details(request, pk):
#     try:
#         list = List.objects.get(pk=pk)
#     except List.DoesNotExist:
#          return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#          serializer = ListSerializer(list)
#          return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ListSerializer(list, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         list.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

     