# Generated by Django 3.1.2 on 2020-12-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0005_auto_20201203_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='tender',
            name='no_of_bidders',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Number of Bidders'),
        ),
    ]
