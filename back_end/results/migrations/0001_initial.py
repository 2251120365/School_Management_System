# Generated by Django 3.0.7 on 2021-01-12 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0005_delete_marksheet'),
        ('students', '0003_student_roll_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjective_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('objective_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('letter_grade', models.CharField(max_length=5)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Exam')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='TabulationSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('total_GP', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('CGPA', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('letter_grade', models.CharField(max_length=5, null=True)),
                ('position', models.PositiveIntegerField(null=True)),
                ('marksheet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='results.MarkSheet')),
            ],
        ),
    ]