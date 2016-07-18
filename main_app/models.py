from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Exco(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("exco"), related_name='exco')
    # slug = AutoSlugField(populate_from="user.username", db_index=False, blank=True)
    position = models.CharField(_("position"), max_length=30, blank=False)
    order = models.IntegerField(_("order"), default=0)
    bio = models.TextField(_("bio"), blank=True)
    contact = models.CharField(_("contact"), max_length=30, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + self.position

    def display_name(self):
        return self.user.first_name + " " + self.user.last_name


class Teacher(models.Model):
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    order = models.IntegerField(_("order"), default=0)
    position = models.CharField(_("position"), max_length=30, blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name + " - " + self.position

    def display_name(self):
        return self.first_name + " " + self.last_name


class User(AbstractUser):
    # Backward compatibility

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
