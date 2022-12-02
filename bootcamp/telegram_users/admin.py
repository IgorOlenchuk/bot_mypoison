from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import TelegramUser, Settings


class TelegramUserAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'tg_name', 'first_name', 'last_name', 'reg_date')
    list_display = ('id', 'tg_name', 'first_name', 'last_name', 'is_respondent', 'reg_date')


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'k_yuany', 'k_comis_1')


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Settings, SettingsAdmin)