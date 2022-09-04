from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from theinkspot.lists.models import List


class ListSerializer(serializers.ModelSerializer):
    user = CurrentUserDefault()

    class Meta:
        model = List
        fields = ("title", "description", "private", "user")
