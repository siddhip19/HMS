# Generated by Django 3.2.6 on 2021-10-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_remove_emergency_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emergency',
            name='requirement',
            field=models.CharField(choices=[('ICU', 'Accident'), ('OXYGEN CYLINDER', 'Stroke/Attack'), ('VENTILATOR', 'Injury')], default='', max_length=50),
        ),
    ]
