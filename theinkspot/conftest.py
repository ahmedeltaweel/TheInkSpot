import pytest

from theinkspot.users.models import User
from theinkspot.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def user2(db) -> User:
    return User.objects.create_user(
        name="user name2",
        username="username2",
        email="test2@email.com",
        password="Am0123456789123456",
    )
