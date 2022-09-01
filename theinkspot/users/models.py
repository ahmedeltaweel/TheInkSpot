from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from theinkspot.category.models import Category


class UserManager(BaseUserManager):
    def create_user(self, username, email, name, password=None):
        if not username:
            raise TypeError("user must have username")
        if not name:
            raise TypeError("user must have name")
        if not email:
            raise TypeError("user must have email")
        if not password:
            raise TypeError("user must have password")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, name, password=None):
        if not username:
            raise TypeError("superuser must have username")
        if not name:
            raise TypeError("superuser must have name")
        if not email:
            raise TypeError("superuser must have email")
        if not password:
            raise TypeError("superuser must have password")
        user = self.model(
            name=name,
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("User Full Name"), max_length=155)
    email = models.EmailField(_("Email"), max_length=155, unique=True)
    username = models.CharField(_("Username"), max_length=155, unique=True)
    is_verified = models.BooleanField(_("Is user verified by email"), default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "email"]

    objects = UserManager()

    def __str__(self):
        return self.username


class UserFollowManager(models.Manager):
    def get_queryset(self):
        # prefetch the followed user and the follower user to avoid 1+N queries
        return super().get_queryset().select_related("followed_user", "follower_user")


class UserFollow(TimeStampedModel):
    follower_user = models.ForeignKey(
        "User", related_name="following", on_delete=models.CASCADE
    )
    followed_user = models.ForeignKey(
        "User", related_name="followers", on_delete=models.CASCADE
    )
    objects = UserFollowManager()

    class Meta:
        unique_together = ("follower_user", "followed_user")

    def save(self, *args, **kwargs):
        # disallow following yourself
        if self.followed_user == self.follower_user:
            raise ValueError("You cannot follow yourself")
        # call super to save the model instance
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.follower_user.username} follows {self.followed_user.username}"


class FollowCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("user", "category")


class UserCategoryFollow(TimeStampedModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="category_follows"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category_followers"
    )
    get_email = models.BooleanField(
        _("get notified about this category"), default=False
    )

    class Meta:
        unique_together = ("user", "category")

    objects = FollowCategoryManager()

    def __str__(self):
        return f"{self.user} follows {self.category}"
