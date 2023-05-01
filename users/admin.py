from django.contrib import admin

from products.admin import BasketAdmin
from users.models import EmailVerification, User

# Регистрируем модель в админке


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerification(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    field = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
