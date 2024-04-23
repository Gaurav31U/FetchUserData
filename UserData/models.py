from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save

class User(AbstractUser):
	username = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	gender = models.CharField(max_length=15)
	skill	= models.TextField()

	def __str__(self):
		return self.name