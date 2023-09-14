from django.contrib import admin
from . import models


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')


@admin.register(models.ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'timestamp')
