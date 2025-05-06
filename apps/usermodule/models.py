from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # hashed password
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
