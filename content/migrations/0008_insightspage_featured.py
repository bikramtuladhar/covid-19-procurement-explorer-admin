# Generated by Django 3.1.2 on 2020-12-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20201223_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='insightspage',
            name='featured',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
