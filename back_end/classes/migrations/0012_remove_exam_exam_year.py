# Generated by Django 3.0.7 on 2021-02-04 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0011_auto_20210201_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_year',
        ),
    ]