# Generated by Django 5.1.1 on 2024-09-26 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='medicalrecord',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='MedicalRecord',
        ),
    ]