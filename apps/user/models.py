import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name=_("email address"))
    is_active = models.BooleanField(default=True, verbose_name=_("active"))
    is_staff = models.BooleanField(default=False, verbose_name=_("staff status"))
    date_joined = models.DateTimeField(default=timezone.now, verbose_name=_("date joined"))

    first_name = models.CharField(max_length=255, verbose_name=_("first name"))
    last_name = models.CharField(max_length=255, verbose_name=_("last name"))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_("birth date"))
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name=("phone"))

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email