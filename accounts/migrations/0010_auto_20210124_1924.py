# Generated by Django 3.1.5 on 2021-01-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210124_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalmodel',
            name='category',
            field=models.IntegerField(null=True),
        ),
    ]
