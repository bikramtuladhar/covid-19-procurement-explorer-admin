# Generated by Django 3.1.2 on 2021-03-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("country", "0026_overallsummary"),
    ]

    operations = [
        migrations.AddField(
            model_name="redflag",
            name="implemented",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
