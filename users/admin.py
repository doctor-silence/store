from django.contrib import admin
from users.models import User

admin.site.register(User)  # Регистрируем модель в админке
