from django.contrib import admin
from . import models
from django.utils.html import format_html, urlencode
from django.urls import reverse

# Register your models here.


@admin.register(models.LicenseType)
class LicenseTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'remarks', 'get_num_employees']

    def get_num_employees(self, obj):
        url = (
            reverse('admin:mis_employee_changelist')
            + '?'
            + urlencode({
                'license_type__id': str(obj.id)
            }))
        return format_html('<a href="{}">{}</a>', url, obj.employee_set.count())

    get_num_employees.short_description = 'تعداد کارمندان'


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
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.EducationalDegree)
class EducationalDegreeAdmin(admin.ModelAdmin):
    list_display = ['title', 'remarks']


class AttachmentInline(admin.TabularInline):
    model = models.Attachment
    extra = 1  # Number of empty attachment forms to display
    readonly_fields = ['thumbnail']
    fields = ['name', 'document', 'thumbnail']

    def thumbnail(self, instance):
        if instance.document.name != '':
            return format_html('<img src="{}" class="thumbnail" width="100px;" />', instance.document.url)
        return ''

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(models.EducationDetails)
class EducationDetailsAdmin(admin.ModelAdmin):
    list_display = ['institute', 'field']


@admin.register(models.EducationalField)
class EducationalFieldAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'remarks']


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline]
    fieldsets = (
        ('معلومات شخصی', {
            'fields': ('name', 'last_name', 'father_name', 'grand_father_name', 'gender', 'nationality', 'id_no'),
        }),
        ('اطلاعات تماس', {
            'fields': ('current_address', 'primary_phone', 'secondary_phone'),
        }),
        ('جزئیات نهاد و جواز مربوطه', {
            'fields': ('organization', 'education', 'license_type', 'license_number', 'license_issue_date', 'license_expiry_date', 'fees'),
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
                    'license_type', 'status', 'view_link')
    search_fields = ['name', 'last_name', 'organization__name']
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def view_link(self, obj):
        url = reverse('mis:employee_detail', args=[obj.pk])
        return format_html('<a href="{}" target="_blank">View</a>', url)

    view_link.short_description = 'View Details'
