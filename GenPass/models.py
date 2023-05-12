from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    AbstractBaseUser,
    PermissionsMixin,
    Group,
    Permission,
)


class User(AbstractUser):
    # Otros campos de usuario aquí
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name="user_groups")

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="user_permissions",
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    # Campos de usuario personalizados aquí


class CustomGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name
