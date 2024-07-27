from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    class Meta:
        permissions = [
                ("user_view", "user_view"),
            ]