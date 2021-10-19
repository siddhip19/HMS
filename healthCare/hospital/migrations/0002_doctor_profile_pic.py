# Generated by Django 2.2.14 on 2021-10-19 19:35

from django.db import migrations, models
import hospital.models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(default='', upload_to=hospital.models.PathAndRename('upload/doctor')),
        ),
    ]
