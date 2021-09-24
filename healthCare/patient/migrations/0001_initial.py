# Generated by Django 3.0.5 on 2021-09-16 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('postal', models.IntegerField()),
                ('dob', models.DateField()),
                ('medical_history', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=15)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Patient')),
            ],
        ),
    ]