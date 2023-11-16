from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class License_Type(models.Model):
    title = models.CharField(max_length=255, verbose_name='نوعیت جواز')
    remarks = models.CharField(
        max_length=255, null=True, blank=True, default='ندارد', verbose_name='ملاحظات')

    class Meta:
        verbose_name = 'نوع جواز'
        verbose_name_plural = 'انواع جوازات'


class Address(models.Model):
    PROVINCE_CHOICES = (
        ('KBL', 'کابل'),
        ('Badakhshan', 'بدخشان'),
        ('Baghlan', 'بغلان'),
        ('Kondoz', 'کندوز'),
        ('Takhar', 'تخار'),
        ('Balkh', 'بلخ'),
        ('Faryab', 'فاریاب'),
        ('Jawzjan', 'جوزجان'),
        ('Samangan', 'سمنگان'),
        ('Sar-e-pol', 'سر پل'),
        ('Bamyan', 'بامیان'),
        ('Kapisa', 'کاپیسا'),
        ('Logar', 'لوگر'),
        ('Panjsher', 'پنجشیر'),
        ('Parwan', 'پروان'),
        ('Maidan-wardak', 'میدان وردګ'),
        ('Konar', 'کنړ'),
        ('Laghman', 'لغمان'),
        ('Noristan', 'نوریستان'),
        ('Badghis', 'بادغیس'),
        ('Farah', 'فراه'),
        ('Ghor', 'غور'),
        ('Herat', 'هرات'),
        ('Ghazni', 'غزنی'),
        ('Khost', 'خوست'),
        ('Paktia', 'پکتیا'),
        ('Paktika', 'پکتیکا'),
        ('Daykondi', 'دایکندی'),
        ('Helmand', 'هلمند'),
        ('Kandahar', 'کندهار'),
        ('Nimroz', 'نیمروز'),
        ('Orozgan', 'اورزګان'),
        ('Zabul', 'زابل'),
        # add more choices here
    )
    DISTRICT_CHOICES = (

        ('1', 'ناحیه اول'),
        ('2', 'ناحیه دوم'),
        ('3', 'ناحیه سوم'),
        ('4', 'ناحیه چهارم'),
        ('5', 'ناحیه پنجم'),
        ('6', 'ناحیه ششم'),
        ('7', 'ناحیه هفتم'),
        ('8', 'ناحیه هشتم'),
        ('9', 'ناحیه نهم'),
        ('10', 'ناحیه دهم'),
        ('11', 'ناحیه یازدهم'),
        ('12', 'ناحیه دوازدهم'),
        ('13', 'ناحیه سیزدهم'),
        ('14', 'ناحیه چهاردهم'),
        ('15', 'ناحیه پانزدهم'),
        ('16', 'ناحیه شانزدهم'),
        ('17', 'ناحیه هفدهم'),
        ('18', 'ناحیه هجدهم'),
        ('19', 'ناحیه نوزدهم'),
        ('20', 'ناحیه بیستم'),
        ('21', 'ناحیه بیست ویکم'),
        # add more choices here
    )
    province = models.CharField(
        max_length=255, choices=PROVINCE_CHOICES, verbose_name="ولایت")
    woleswali = models.CharField(
        max_length=255, default='کابل', verbose_name='ولسوالی')
    district = models.CharField(
        max_length=255, choices=DISTRICT_CHOICES, verbose_name="ناحیه")
    road = models.CharField(
        max_length=255, verbose_name="سرک", default='ندارد')
    avenue = models.CharField(
        max_length=255, verbose_name="کوچه", default='ندارد')

    def __str__(self):
        return self.province + ' '+self.district

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'


class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام')
    owner_name = models.CharField(
        max_length=255, verbose_name='نام صاحب امتیاز')
    owner_father_name = models.CharField(
        max_length=255, verbose_name='ولد صاحب امتیاز')
    owner_grand_father_name = models.CharField(
        max_length=255, verbose_name='ولدیت صاحب امتیاز')
    owner_tazkira_number = models.CharField(
        max_length=255, verbose_name='تذکره نمبر صاحب امتیاز')
    address = models.CharField(
        max_length=255, default='null', verbose_name='آدرس محل')
    contact = models.CharField(
        max_length=10, blank=True, null=True, help_text='0784009003', verbose_name='شماره تماس')
    remarks = models.TextField(
        max_length=255, verbose_name='ملاحظات', default='null')
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='payment_plans_payment_created', null=True, verbose_name="ایجاد شد")
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='payment_plans_payment_updated', null=True, verbose_name="تغییر شد")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ایجاد", null=True)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="زمان تغییر", null=True)

    class Meta:
        verbose_name = 'نهاد صحی'
        verbose_name_plural = 'تاسیسات صحی'

    def __str__(self):
        return self.name
