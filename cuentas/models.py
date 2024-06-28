from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=settings.ROLES)

    def str(self):
        return self.user.username + ' - '+self.role
# Create your models here.
