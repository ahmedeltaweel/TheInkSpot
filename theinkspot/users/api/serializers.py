from pkg_resources import require
from dataclasses import dataclass
from typing import List
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }
