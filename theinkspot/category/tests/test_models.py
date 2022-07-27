import pytest
from django.db import IntegrityError

from theinkspot.category.models import Category, UserCategoryFollow

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


@pytest.mark.django_db
class TestUserCategoryFollow:
    def test_UserCategoryFollow_unique_together(self):
        unique_together = UserCategoryFollow._meta.unique_together
        assert unique_together[0] == ("user", "category")

    def test_UserCategoryFollow_ordering(self):
        unique_together = UserCategoryFollow._meta.ordering
        assert unique_together[0] == "-created_at"

    def test_user_follow_category(self, user, category):
        follow = UserCategoryFollow.objects.create(user=user, category=category)
        assert user.followers.count() == 1
        assert category.followed_categories.count() == 1
        assert follow.get_email is False

    def test_get_email_label(self):
        label = UserCategoryFollow._meta.get_field("get_email").verbose_name
        assert label == "Get notified with top posts"

    def test_get_email_default_value(self):
        default = UserCategoryFollow._meta.get_field("get_email").default
        assert default is False

    def test_user_unfollow_category(self, user, category):
        UserCategoryFollow.objects.create(user=user, category=category)
        user.followers.first().delete()
        assert user.followers.count() == 0
        assert category.followed_categories.count() == 0

    def test_user_follow_already_followed_category(self, user, category):
        UserCategoryFollow.objects.create(user=user, category=category)

        with pytest.raises(IntegrityError):
            UserCategoryFollow.objects.create(user=user, category=category)

    def test_user_unfollow_already_unfollowed_category(self, user, category):
        UserCategoryFollow.objects.create(user=user, category=category)
        user.followers.first().delete()

        with pytest.raises(AttributeError):
            user.followers.first().delete()

    def test_object_name_is_user_follows_category(self, user, category):
        follow = UserCategoryFollow.objects.create(user=user, category=category)
        assert str(follow) == f"{follow.user} follows {follow.category}"
