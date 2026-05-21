from django.db import models


from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    image = models.ImageField(
        upload_to='users/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
        




 