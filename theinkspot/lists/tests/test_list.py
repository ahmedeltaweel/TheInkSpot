import pytest
from rest_framework.test import APIClient, APITestCase

from theinkspot.users.models import User

client = APIClient()


@pytest.mark.django_db
class TestListCreationView(APITestCase):
    def test_adding_list(self):
        self.user = User.objects.create(
            username="testuser",
            email="testuser@gmail.com",
            password="ABc_123",
        )

        data = {
            "title": "blogs",
            "description": "this is list of blogs",
            "private": True,
            "user": self.user.id,
        }
        response = client.post("/lists/", data, format="json")
        payload = response.data
        assert response.status_code == 201
        assert payload["title"] == data["title"]
        assert payload["description"] == data["description"]
        assert payload["private"] == data["private"]

    def test_add_list_without_title(self):
        self.user = User.objects.create(
            username="testuser",
            email="testuser@gmail.com",
            password="ABc_123",
        )
        data = {
            "title": "",
            "description": "this is list of Articles",
            "private": "True",
            "user": self.user.id,
        }
        response = client.post("/lists/", data)
        payload = response.data
        assert payload["title"][0] == "This field may not be blank."
        assert response.status_code == 400

    def test_list_update(self):
        self.user = User.objects.create(
            username="testuser",
            email="testuser@gmail.com",
            password="ABc_123",
        )
        data = {"title": "aa", "user": self.user.id}

        response = client.post("/lists/", data, format="json")
        assert response.status_code == 201
