# Generated by Django 3.0.7 on 2021-01-15 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_auto_20210115_0127'),
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exam',
            new_name='ExamType',
        ),
        migrations.RenameField(
            model_name='examtype',
            old_name='exam_name',
            new_name='exam_type',
        ),
    ]
