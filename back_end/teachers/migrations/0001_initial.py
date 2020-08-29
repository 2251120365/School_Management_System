# Generated by Django 3.0.7 on 2020-06-15 14:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('username', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('duplicate_name_count', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('NID_no', models.CharField(max_length=100, verbose_name='NID no.:')),
                ('designation', models.CharField(max_length=100)),
                ('present_address', models.TextField()),
                ('office_telephone', models.CharField(max_length=13, verbose_name='Telephone no.(Office)')),
                ('home_telephone', models.CharField(max_length=13, verbose_name='Telephone no.(Home)')),
                ('office_mobile', models.CharField(max_length=11, verbose_name='Mobilephone no.(Office)')),
                ('personal_mobile', models.CharField(max_length=11, verbose_name='Mobilephone no.(Personal)')),
                ('fax', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=50)),
                ('date_of_join', models.DateField()),
                ('date_of_birth', models.DateField()),
                ('marital_status', models.CharField(choices=[('MR', 'Married'), ('UM', 'Unmarried')], max_length=2)),
                ('permanent_address', models.TextField()),
                ('highest_educational_qualification', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(9999)])),
                ('institute', models.CharField(max_length=70)),
                ('board', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=10)),
                ('id_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher')),
            ],
        ),
    ]
