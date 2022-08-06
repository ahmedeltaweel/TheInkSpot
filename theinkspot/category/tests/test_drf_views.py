import pytest
from rest_framework.test import APIClient

from theinkspot.category.models import Category

pytestmark = pytest.mark.django_db
client = APIClient()


@pytest.mark.django_db
class TestCategoryViewSet:
    def test_list_categories(self, category):
        request = client.get("/api/category/")
        assert request.status_code == 200

    def test_retrive_category(self, category):
        id = Category.objects.get(name="sports").id
        request = client.get(f"/api/category/{id}/")
        assert request.status_code == 200
