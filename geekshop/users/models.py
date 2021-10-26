from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.utils.timezone import now

NULL_INSTALL ={'blank':True,'null':True}
class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    activation_key = models.CharField(max_length=128,**NULL_INSTALL)
    age = models.PositiveIntegerField(default=18)
    activation_key_created = models.DateTimeField(default=(now()+timedelta(hours=48)),**NULL_INSTALL)

    def is_activation_key_expired(self):
        if now()<= self.activation_key_created+timedelta(hours=48):
            return False
        return True

