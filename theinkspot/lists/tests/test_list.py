import pytest
from rest_framework.test import APIClient, APITestCase

from theinkspot.lists.models import List
from theinkspot.users.models import User

client = APIClient()


@pytest.mark.django_db
class TestListCreationView(APITestCase):
    def make_list(self):
        self.user = User.objects.create(
            username="testuser",
            email="testuser@gmail.com",
            password="ABc_123",
        )
        list = List(
            title="blogs",
            description="this is list of blogs",
            private=True,
            user=self.user,
        )
        list.save()
        return list

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
            "user": self.user,
        }
        response = client.post("/lists/", data)
        payload = response.data
        assert payload["title"][0] == "This field may not be blank."
        assert response.status_code == 400

    def test_list_update_not_from_anonymous_users(self):
        list = self.make_list()
        response = self.client.put("/lists/" + str(list.id) + "/", args=[list.id])
        assert response.status_code == 401

    def test_list_partial_update_from_anonymous_users(self):
        list = self.make_list()
        response = self.client.patch("/lists/" + str(list.id) + "/", args=[list.id])
        assert response.status_code == 401

    def test_list_delete_from_anonymous_users(self):
        list = self.make_list()
        response = self.client.delete("/lists/" + str(list.id) + "/", args=[list.id])
        assert response.status_code == 401

    def test_list_retrieve_for_anonymous_users(self):
        list = self.make_list()
        response = self.client.get("/lists/" + str(list.id) + "/", args=[list.id])
        assert response.status_code == 200
