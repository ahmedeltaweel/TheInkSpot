from django.db import models
from django.utils.translation import gettext_lazy as _

from theinkspot.users.models import User


class Category(models.Model):
    CATEGORIES = [
        ("sports", "Sports"),
        ("computer science", "Computer Science"),
        ("Physics", "Physics"),
        ("space", "Space"),
        ("cinema", "Cinema"),
        ("music", "Music"),
        ("economy", "Economy"),
    ]

    name = models.CharField(
        _("Category Name"), max_length=50, choices=CATEGORIES, unique=True
    )

    def __str__(self):
        return f"{self.name}"


class UserCategoryFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="followed_categories"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    get_email = models.BooleanField(_("Get notified with top posts"), default=False)

    class Meta:
        unique_together = ("user", "category")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} follows {self.category}"
