from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator
from .managers import CustomerManager, EmployeeManager, AdministratorManager


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True, null=True, blank=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(
        _('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]


class Administrator(User):
    objects = AdministratorManager()
    class Meta:
        proxy = True
        verbose_name = _('administrator')
        verbose_name_plural = _('administrators')
