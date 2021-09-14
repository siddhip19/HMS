# Generated by Django 3.0.5 on 2021-09-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('phone', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
