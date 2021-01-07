# Generated by Django 3.0.7 on 2021-01-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('home_background', models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Homepage background photo')),
                ('home_photo_1', models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Homepage photo 1')),
                ('home_photo_2', models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Homepage photo 1')),
                ('home_photo_3', models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Homepage photo 1')),
                ('home_photo_4', models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Homepage photo 1')),
                ('overview', models.TextField(blank=True, null=True)),
                ('academic_overview', models.TextField(blank=True, null=True)),
                ('academic_photo', models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Academic page photo')),
            ],
        ),
    ]
