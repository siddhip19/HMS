# Generated by Django 3.2 on 2021-10-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_appointment_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default=False, max_length=5),
        ),
    ]
