import os

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from .managers import UserManager
from .utils import user_media_path, user_media_cover_path


class User(AbstractBaseUser, PermissionsMixin):
    """ user model
    """
    email = models.EmailField(max_length=500, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    title = models.CharField(max_length=50, null=True, blank=True)
    handle = models.CharField(max_length=150)
    bio = models.TextField(null=True, blank=True)

    subscribers = models.ManyToManyField('self', blank=True)

    image = models.ImageField(upload_to=user_media_path, null=True, blank=True)
    cover = models.ImageField(upload_to=user_media_cover_path, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")
    _image = _cover = None

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.handle = self.trimmed_email

        return super(User, self).save(*args, **kwargs)

    def delete_image(self, image, location):
        os.remove(f"{image.path}") if os.path.exists(f"{image.path}") else None

    def get_short_name(self):
        return f"{self.first_name}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".title()

    @property
    def get_display_name(self):
        if self.first_name and self.last_name:
            return self.get_full_name
        return f"{self.email}"

    @property
    def trimmed_email(self):
        return self.email.split("@")[0]


@receiver(pre_save, sender=User)
def auto_remove_imagefile(sender, instance=None, **kwargs):
    user = User.objects.get(id=instance.id)

    # check if there is a new uploaded image.
    if user.image and instance.image != user.image:
        instance.delete_image(user.image, 'avatar')

    # # check if there is a new uploaded cover
    if user.cover and instance.cover != user.cover:
        instance.delete_image(user.cover, 'cover')




