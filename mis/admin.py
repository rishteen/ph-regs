from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.License_Type)
class LicenseTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'remarks']


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['province', 'district', 'road', 'avenue']
    fields = ('province', 'district', 'road', 'avenue')
    search_fields = ['province', 'district']


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner_name']
