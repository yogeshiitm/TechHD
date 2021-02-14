# Generated by Django 3.1.5 on 2021-02-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalmodel',
            name='dose_status',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='medicalmodel',
            name='vaccination_status',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
