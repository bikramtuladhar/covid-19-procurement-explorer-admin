# Generated by Django 3.1.2 on 2021-01-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_auto_20210105_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrypartner',
            name='description',
            field=models.CharField(max_length=500000, unique=True, verbose_name='Description'),
        ),
    ]
