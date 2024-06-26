from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class LicenseType(models.Model):
    title = models.CharField(max_length=255, verbose_name='نوعیت جواز')
    remarks = models.CharField(
        max_length=255, null=True, blank=True, default='ندارد', verbose_name='ملاحظات')

    class Meta:
        verbose_name = 'نوع جواز'
        verbose_name_plural = 'انواع جوازات'

    def __str__(self):
        return self.title


class EducationalField(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان رشته')

    class Meta:
        verbose_name = 'رشته'
        verbose_name_plural = 'رشته ها'

    def __str__(self):
        return self.title


class EducationalDegree(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    remarks = models.TextField(blank=True, null=True, verbose_name='نوت')

    class Meta:
        verbose_name = 'نوع مدرک تحصیلی'
        verbose_name_plural = 'انواع مدارک تحصیلی'

    def __str__(self):
        return self.title


class EducationDetails(models.Model):
    institute = models.CharField(max_length=255, verbose_name='مرجع')
    field = models.ForeignKey(
        EducationalField, on_delete=models.CASCADE, verbose_name='تخصصي څانګه')
    year_of_graduation = models.DateField(verbose_name='د فراغت کال')
    license_no = models.CharField(
        max_length=255, verbose_name='د دیپلوم شمیره')
    license_type_diplom = models.ForeignKey(
        EducationalDegree, on_delete=models.CASCADE, verbose_name='دیپلوم')

    class Meta:
        verbose_name = 'تخصصي معلومات'
        verbose_name_plural = 'تخصصي معلومات'

    def __str__(self):
        return f"{self.institute} | {self.license_no}"


class Fees(models.Model):
    title = models.CharField(max_length=255, verbose_name='دې فیس کتګوري')
    price = models.PositiveIntegerField(verbose_name="بیه")
    remarks = models.CharField(
        max_length=255, verbose_name='نوټ', default='نلري')

    class Meta:
        verbose_name = 'د فیس بیه'
        verbose_name_plural = 'د فیس بیه'

    def __str__(self):
        return f"{self.title}|{self.price}"


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

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    def __str__(self):
        return f"{self.province} - {self.district}"


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
        User, on_delete=models.SET_NULL, related_name='organization_created', null=True, verbose_name="ایجاد شد")
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='organization_updated', null=True, verbose_name="تغییر شد")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ایجاد", null=True)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="زمان تغییر", null=True)

    class Meta:
        verbose_name = 'نهاد صحی'
        verbose_name_plural = 'تاسیسات صحی'

    def __str__(self):
        return self.name


class Employee(models.Model):
    GENDER_CHOICES = (
        ('Male', 'مرد'),
        ('Female', 'زن'),
        ('Other', 'دیگر')
    )
    NATIONALITY_CHOICES = (
        ('Afghan', 'افغان'),
        ('Khariji', 'خارجی')
    )
    name = models.CharField(max_length=255, verbose_name="اسم")
    last_name = models.CharField(max_length=255, verbose_name="تخلص")
    father_name = models.CharField(max_length=255, verbose_name="ولد")
    grand_father_name = models.CharField(
        max_length=255, null=True, blank=True, default='خالی', verbose_name="ولدیت")
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, verbose_name="جنسیت")
    nationality = models.CharField(
        max_length=10, choices=NATIONALITY_CHOICES, verbose_name="ملیت")
    id_no = models.CharField(max_length=20, unique=True,
                             verbose_name="تذکره / پاسپورت نمبر")
    current_address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name='employees', verbose_name="آدرس")
    primary_phone = models.CharField(max_length=15, verbose_name="شماره تماس")
    secondary_phone = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="شماره تماس دوم")
    organization = models.ForeignKey(
        Organization, on_delete=models.PROTECT, verbose_name='نهاد صحی')
    education = models.ForeignKey(
        EducationDetails, on_delete=models.PROTECT, verbose_name='سطح تحصیلی')
    license_type = models.ForeignKey(
        LicenseType, on_delete=models.PROTECT, verbose_name='نوعیت جواز')
    fees = models.ForeignKey(
        Fees, on_delete=models.CASCADE, verbose_name='تعیین شوۍ فیس')
    license_number = models.CharField(
        max_length=20, verbose_name='شماره جواز', unique=True)
    license_issue_date = models.DateField(verbose_name="تاریخ صدور جواز")
    license_expiry_date = models.DateField(verbose_name="تاریخ انقضای جواز")
    status = models.BooleanField(default=True, verbose_name="فعال/غیر فعال")
    qr_code = models.ImageField(
        upload_to='qr_codes', blank=True, null=True, verbose_name="کیو ار کد")
    photo = models.ImageField(
        upload_to='services/customer/images', blank=True, null=True, verbose_name="عکس")
    remarks = models.TextField(
        blank=True, null=True, verbose_name="ملاحظات", default='ملاحظه ای ندارد!')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   related_name='employee_created', null=True, verbose_name="ایجاد شد")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   related_name='employee_updated', null=True, verbose_name="تغییر شد")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ایجاد", null=True)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="زمان تغییر", null=True)

    class Meta:
        verbose_name = 'کدر صحی'
        verbose_name_plural = 'کدر ها'

    def __str__(self):
        return f"{self.name} - {self.last_name} - {self.organization}"


class Attachment(models.Model):
    name = models.CharField(max_length=255, verbose_name='عنوان')
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='attachments', verbose_name='سند')
    document = models.FileField(upload_to='attachment/files')
    uploaded_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='ایجاد شد')
    uploaded_at = models.DateTimeField(
        default=timezone.now, verbose_name='زمان اپلود شد')

    class Meta:
        verbose_name = 'فایل ضمیمه'
        verbose_name_plural = 'ضمیمه ها'

    def __str__(self):
        return self.name
