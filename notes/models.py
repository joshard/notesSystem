from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    entry_date = models.DateTimeField(auto_now=True)