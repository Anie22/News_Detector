from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("please enter a valid email address"))

    def create_user(self, full_name, user_name, email, password, **extra_fields):
        if not full_name:
            raise ValueError(_("full name required"))

        if not user_name:
            raise ValueError(_("user name required"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("email address is required"))

        user = self.model(
            full_name = full_name,
            user_name = user_name,
            email = email,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, full_name, user_name, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)

        if not password:
            raise ValueError(_('password required'))

        user = self.create_user(
            full_name = full_name,
            user_name = user_name,
            email = email,
            password = password,
            **extra_fields
        )

        user.save(using=self._db)

        return user