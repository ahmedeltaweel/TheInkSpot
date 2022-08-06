import pytest
from rest_framework.test import APIClient, APITestCase

client = APIClient()


@pytest.mark.django_db
class TestListCreationView(APITestCase):
    def test_adding_list(self):
        data = {
            "title": "blogs",
            "description": "this is list of blogs",
            "private": True,
        }
        response = client.post("/lists/listview/", data, format="json")
        payload = response.data
        assert response.status_code == 200
        assert payload["data"]["title"] == data["title"]
        assert payload["data"]["description"] == data["description"]
        assert payload["data"]["private"] == data["private"]

    def test_add_list_without_title(self):
        data = {
            "title": "",
            "description": "this is list of Articles",
            "private": "True",
        }
        response = client.post("/lists/listview/", data)
        assert response.status_code == 400

    def test_list_update(self):
        data = {
            "title": "aa",
        }

        response = client.post("/lists/listview/", data, format="json")
        assert response.status_code == 200
