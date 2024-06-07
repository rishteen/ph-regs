# Generated by Django 5.0.6 on 2024-06-07 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0002_alter_attachment_options_alter_employee_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان رشته')),
            ],
            options={
                'verbose_name': 'رشته',
                'verbose_name_plural': 'رشته ها',
            },
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='دې فیس کتګوري')),
                ('price', models.PositiveIntegerField(verbose_name='بیه')),
                ('remarks', models.CharField(default='نلري', max_length=255, verbose_name='نوټ')),
            ],
            options={
                'verbose_name': 'د فیس بیه',
                'verbose_name_plural': 'د فیس بیه',
            },
        ),
        migrations.CreateModel(
            name='EducationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institude', models.CharField(max_length=255, verbose_name='مرجع')),
                ('year_of_graduation', models.DateField(verbose_name='د فراغت کال')),
                ('license_no', models.CharField(max_length=255, verbose_name='د دیپلوم شمیره')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.educationalfield', verbose_name='تخصصي څانګه')),
                ('license_type_diplom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.educational_degree', verbose_name='دیپلوم')),
            ],
            options={
                'verbose_name': 'تخصصي معلومات',
                'verbose_name_plural': 'تخصصي معلومات',
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mis.educationdetails', verbose_name='سطح تحصیلی'),
        ),
    ]
