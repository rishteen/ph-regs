from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.License_Type)
class LicenseTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'remarks']
