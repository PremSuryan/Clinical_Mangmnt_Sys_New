# Generated by Django 4.2.2 on 2024-06-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCentre', '0012_alter_doctor_passwordhash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='passwordHash',
            field=models.CharField(max_length=64),
        ),
    ]