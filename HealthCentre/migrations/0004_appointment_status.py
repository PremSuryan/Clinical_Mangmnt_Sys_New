# Generated by Django 4.2.2 on 2024-06-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthCentre', '0003_remove_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
