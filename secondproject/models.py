from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class SecondAdminUser(AbstractUser):
    """A separate User model for the second project's admin panel"""

    second_project_only = models.BooleanField(default=True)  # Just an example field

    groups = models.ManyToManyField(
        Group,
        related_name="second_admin_users",  # Custom related name to avoid conflict
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="second_admin_users_permissions",  # Custom related name to avoid conflict
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )
