# Generated by Django 3.0.7 on 2021-02-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0019_routine_saturday'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='board_exam_evaluation',
            field=models.BooleanField(default=False),
        ),
    ]