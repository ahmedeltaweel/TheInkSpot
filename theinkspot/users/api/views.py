from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from theinkspot.users.models import List
from rest_framework.views import APIView 
from rest_framework import status
from django.http import Http404
from theinkspot.users.models import List
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, ListSerializer


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

    permission_classes = [AllowAny] 
    serializer_class = ListSerializer   
 
    def post(self, request):
        user = request.user
        list = request.data
        username = User.objects.filter(username=user.username).first()
        serializer = self.serializer_class(username, data=list)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                 status=status.HTTP_200_OK
                 )
        else:
            return Response(
                {"status": "error", "data": serializer.errors}, 
                status=status.HTTP_400_BAD_REQUEST
                )
 

 
class ListDetailsView(APIView):
    def retrieve(self, request, pk): 
        permission_classes = [AllowAny] 
        user = request.user
        if(user.is_authenticated):
            try:
                list = List.objects.get(pk=pk)
            except List.DoesNotExist:
                raise Http404("Not exist.") 
            serializer = ListSerializer(list)
            serializer.save()   
            return Response(serializer.data)
        else:
            raise AuthenticationFailed("Please, Login First")
 
 