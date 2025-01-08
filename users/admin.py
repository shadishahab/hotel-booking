from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Person


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username','first_name', 'last_name', 'date_joined']
    list_display_links = ['id', 'username']


class PersonAdmin(UserAdmin):
    list_display = ['id', 'user', 'gender','phone_number', 'birth_date',]
    list_display_links = ['id', 'user']

admin.site.register(Person, PersonAdmin)
admin.site.register(CustomUser, CustomUserAdmin)