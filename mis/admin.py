from django.contrib import admin
from . import models
from django.utils.html import format_html, urlencode
from django.urls import reverse
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
    list_display = ['name', 'owner_name', 'get_num_employees',
                    'address', 'created_by', 'created_at']
    fields = ['name', 'owner_name', 'owner_father_name', 'owner_grand_father_name',
              'owner_tazkira_number', 'address', 'contact', 'remarks']

    def get_num_employees(self, obj):
        url = (
            reverse('admin:mis_employee_changelist')
            + '?'
            + urlencode({
                'organization__id': str(obj.id)
            }))
        return format_html('<a href="{}">{}</a>', url, obj.employee_set.count())

    get_num_employees.short_description = 'تعداد کارمندان'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.Educational_Degree)
class EducationalDegreeAdmin(admin.ModelAdmin):
    list_display = ['title', 'remarks']


class AttachmentInline(admin.TabularInline):
    readonly_fields = ['created_by', 'created_by']
    fields = ['name', 'document', 'thumbnail']
    model = models.Attachment
    extra = 1  # Number of empty attachment forms to display
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.document.name != '':
            return format_html(f'<img src="{instance.document.url}" class="thumbnail" />')
        return ''

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline]
    fieldsets = (
        ('معلومات شخصی', {
            'fields': ('name', 'last_name', 'father_name', 'grand_father_name', 'gender', 'nationaliy', 'id_no'),
        }),
        ('اطلاعات تماس', {
            'fields': ('current_address', 'primary_phone', 'secondary_phone'),
        }),
        ('جزئیات نهاد و جواز مربوطه', {
            'fields': ('organization', 'education', 'license_type', 'license_number', 'license_issue_date', 'license_expiry_date'),
        }),
        ('Status and Additional Details', {
            'fields': ('status', 'qr_code', 'photo', 'remarks'),
        }),
        ('User and Timestamps', {
            'fields': ('created_by', 'updated_by', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    list_display = ('name', 'last_name', 'organization',
                    'status', 'created_at', 'updated_at')
    search_fields = ['name', 'last_name', 'organization__name']
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        super().save_model(request, obj, form, change)
