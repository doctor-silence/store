from django.urls import path
from users.views import login, registration

app_name = 'users'

# Добавляем новые урлы
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
]
