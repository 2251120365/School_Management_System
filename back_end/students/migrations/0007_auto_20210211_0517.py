# Generated by Django 3.0.7 on 2021-02-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20210211_0447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='employed_guardian_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='previous_class',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tc_number',
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
