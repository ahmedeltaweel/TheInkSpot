from rest_framework import serializers

from theinkspot.lists.models import List
from rest_framework.fields import CurrentUserDefault


class ListSerializer(serializers.ModelSerializer):
    user = CurrentUserDefault()

    class Meta:
        model = List
        fields = ("title", "description", "private", "user")
