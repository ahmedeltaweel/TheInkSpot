from wsgiref import validate
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from users.validators import validate_facebook


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
    fb_url = models.URLField(_("Facebook link"), max_length=100, validators=[validate_facebook])
    # twitter_url = models.URLField(_("Twitter link"), max_length=100)
    # gh_url = models.URLField(_("Github Link"), max_length=100)
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
