# Generated by Django 3.0.7 on 2021-02-04 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_sessions', '0001_initial'),
        ('institution', '0005_institution_current_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='current_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academic_sessions.Session'),
        ),
    ]