from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a 'user profile' inside our system."""
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length=255)
    is_activate = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Used to get users full name. """

        return self.name
    
    def get_short_name(self):
        """ Used to get user short name."""

        return self.name

    def __str__(self):
        """ Django uses this when it need to convert the objectt to a string"""

        return self.email
    
    