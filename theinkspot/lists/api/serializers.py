
from pkg_resources import require
from dataclasses import dataclass
#from typing import List
from rest_framework import serializers
from theinkspot.lists.models import List
 
 
class ListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=False)
    description = serializers.CharField(max_length=500, required=False)
    public = serializers.BooleanField(default=True)
    class Meta:
        model = List
        fields = ("title", "description", "public")
   
    def create_list(self, username, **validated_data ):
        list = List.objects.create(
            username=username,
            title=validated_data["title"],
            description=validated_data["description"],
            created=validated_data["created"],  
            public=validated_data["public"],  
        )
        return list