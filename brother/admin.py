from django.contrib import admin

# Register your models here.

from .models import User, Device, Log

admin.site.register(User)
admin.site.register(Device)
admin.site.register(Log)