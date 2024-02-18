from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, PrimaryGroup, SaveAddress

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(PrimaryGroup)
admin.site.register(SaveAddress)