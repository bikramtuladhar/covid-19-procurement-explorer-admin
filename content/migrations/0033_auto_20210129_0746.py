# Generated by Django 3.1.2 on 2021-01-29 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0032_auto_20210129_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcespage',
            name='link',
            field=models.URLField(blank=True, max_length=10000, null=True),
        ),
    ]
