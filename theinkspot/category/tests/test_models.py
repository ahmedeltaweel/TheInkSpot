import pytest
from django.db import IntegrityError

from theinkspot.category.models import Category

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestCategoryModel:
    def test_object_name_is_first_name(self, category):
        object_name = f"{category.name}"
        assert str(category) == object_name

    def test_category_name_label(self, category):
        name_label = category._meta.get_field("name").verbose_name
        assert name_label == "Category Name"

    def test_unique_constraint_on_name_is_true(self, category):
        unique = category._meta.get_field("name").unique
        assert unique is True

    def test_unique_constriant_on_category_name(self, category):
        with pytest.raises(IntegrityError):
            Category.objects.create(name="sports")

    def test_name_max_length(self):
        max_length = Category._meta.get_field("name").max_length
        assert max_length == 50

    def test_create_category(self, category):
        assert Category.objects.filter(name="sports").count() == 1
