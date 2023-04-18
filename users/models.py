from django.db import models
from django.contrib.auth.models import AbstractUser

# Добавляем новые поля в модель Юзер
class User(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)