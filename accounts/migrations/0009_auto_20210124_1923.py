# Generated by Django 3.1.5 on 2021-01-24 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210124_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalmodel',
            options={'ordering': ['category']},
        ),
        migrations.RenameField(
            model_name='medicalmodel',
            old_name='eligibility_score',
            new_name='illness_score',
        ),
    ]
