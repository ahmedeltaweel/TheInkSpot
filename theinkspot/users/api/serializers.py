from dataclasses import dataclass
from typing import List
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.timezone import now
from theinkspot.users.models import List

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

 
 
class ListSerializer(serializers.ModelSerializer):
    title = serializers.CharField( max_length= 100)
    description = serializers.CharField( max_length= 500)
    public = serializers.BooleanField(default= True)
    class Meta:
        model = List
        fields = ("title", "description", "public")
 
 
    def validate(self, data):
        if not data.get("title"):
            raise serializers.ValidationError(
               {"Unacceptable, Lists must have a title"}
            )
        return data    
 
 
    def create_list(self, username,**validated_data ):
        list = List.objects.create(
            username = username, 
            title = validated_data["title"], 
            description = validated_data["description"],
            created = validated_data["created"],   
            public= validated_data["public"],  
         )
        return list
 
 
 




