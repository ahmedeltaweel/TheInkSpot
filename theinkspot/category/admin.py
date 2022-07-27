from django.contrib import admin

from theinkspot.category.models import Category, UserCategoryFollow


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Category, CategoryAdmin)


class UserCategoryFollowAdmin(admin.ModelAdmin):
    list_display = ["user", "category", "get_email", "created_at"]


admin.site.register(UserCategoryFollow, UserCategoryFollowAdmin)
