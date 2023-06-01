from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """ Class for User information and details """

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nickname = models.CharField(max_length=40)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)