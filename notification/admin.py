from django.contrib import admin
from .models import Notification, Viewed
# Register your models here.

admin.site.register(Notification)
admin.site.register(Viewed)