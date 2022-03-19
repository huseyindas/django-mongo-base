from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not password:
            raise ValueError(_("Users must have a password"))
        email = self.normalize_email(email)

        user_create_fields = {"email": email}
        user = self.model(**user_create_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
