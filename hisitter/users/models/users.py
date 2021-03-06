"""User model module."""

# Django imports
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.conf import settings
from django.db import models

# Utils Abstract model
from hisitter.utils.abstract_users import HisitterModel


class User(AbstractUser, HisitterModel):
    """ Default user for hisitter.

        Extend from django's Abstract user, change the username field
        to email and add some extra fields.
    """
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists'
        },
    )
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{10,12}',
        message="Phone number must be entered in 10 digits format."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        blank=False
    )
    picture = models.ImageField(
        'user picture',
    )
    birthdate = models.DateField(
        'birthdate',
        blank=False
    )
    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to True when the user have verified its email address'
    )
    reputation = models.DecimalField(
        default=5.0,
        max_digits=2,
        decimal_places=1,
        help_text="User's reputation bases on the services."
    )
    address = models.CharField(
        max_length=255,
        blank=False
    )
    lat = models.DecimalField(
        _("Latitude"),
        max_digits=10,
        decimal_places=6,
        blank=True,
        null=True
    )
    long =  models.DecimalField(
        _("Latitude"),
        max_digits=10,
        decimal_places=6,
        blank=True,
        null=True
    )
    GENRES = [
        ('male', 'male'),
        ('female', 'female'),
        ('unspecified', 'unspecified')
    ]
    genre = models.CharField(
        max_length=11,
        choices=GENRES,
        default='unspecified'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'birthdate', 'address', 'phone_number']

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    def __str__(self):
        """Return user's str representation."""
        return self.username + ', ' + self.email

    class Meta:
        ordering = ['-reputation']
