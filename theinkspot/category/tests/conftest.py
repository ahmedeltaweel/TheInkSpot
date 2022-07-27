import pytest

from theinkspot.category.models import Category
from theinkspot.users.models import User


@pytest.fixture()
def category(db) -> Category:
    return Category.objects.create(name="sports")


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(
        name="user name",
        username="username",
        email="test@email.com",
        password="Am0123456789123456",
    )
