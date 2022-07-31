import pytest
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from config.settings.local import SECRET_KEY
from theinkspot.users.models import List, UserManager
from theinkspot.users.views import User

client = APIClient()
 

@pytest.mark.django_db
class TestListCreationView(APITestCase):
    def test_adding_list(self):
        user = User.objects.filter(username="mariamelhadad").first()
       
        data = {
            "title": "blogs",
            "description": "this is list of blogs",
            "public": True,
         }
        response = client.post("/users/create/lists/", data, format="json")
 
        payload = response.data
        assert response.status_code == 200
        assert payload["data"]["title"] == data["title"]
        assert payload["data"]["description"] == data["description"]
        assert payload["data"]["public"] == data["public"]
 
    def test_add_list_without_title(self):
    
        data = {
            "title": "",
            "description": "this is list of Articles",
            "public": "True",
        }
 
        response = client.post("/users/create/lists/", data)    
        assert response.status_code == 400