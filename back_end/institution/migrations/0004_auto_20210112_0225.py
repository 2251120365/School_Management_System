# Generated by Django 3.0.7 on 2021-01-12 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0003_auto_20210108_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='home_photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Homepage Photo 2'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='home_photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Homepage Photo 3'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='home_photo_4',
            field=models.ImageField(blank=True, null=True, upload_to='photos/others/%Y/%m/%d/', verbose_name='Homepage Photo 4'),
        ),
    ]
