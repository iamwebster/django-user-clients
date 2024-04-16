from django.contrib import admin
from django.contrib.auth.apps import AuthConfig
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin

from .models import Client 


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'responsible', 'status']
    list_editable = ['status']


admin.site.unregister(User)
admin.site.unregister(Group)

AuthConfig.verbose_name = "Пользователи"


class ClientInline(admin.StackedInline):
    model = Client
    extra = 1


@admin.register(User)
class UserCustomAdmin(UserAdmin):
    list_display = ['username', 'is_staff']
    fieldsets = [
        (None, {
            'fields': ('username', 'password', 'is_staff', 'is_superuser')
        })]
    inlines = [ClientInline,]
