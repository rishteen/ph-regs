from django.db import models

# Create your models here.


class License_Type(models.Model):
    title = models.CharField(max_length=255, verbose_name='نوعیت جواز')
    remarks = models.CharField(
        max_length=255, null=True, blank=True, default='ندارد', verbose_name='ملاحظات')

    class Meta:
        verbose_name = 'نوع جواز'
        verbose_name_plural = 'انواع جوازات'
