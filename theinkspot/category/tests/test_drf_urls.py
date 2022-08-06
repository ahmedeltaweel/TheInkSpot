import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_lsit_category_url():
    assert reverse("api:category-list") == "/api/category/"
    assert resolve("/api/category/").view_name == "api:category-list"


def test_verify_email_url():
    pk = 1
    assert (
        reverse(
            "api:category-detail",
            args=[
                pk,
            ],
        )
        == "/api/category/1/"
    )
    assert resolve("/api/category/<pk>/").view_name == "api:category-detail"
