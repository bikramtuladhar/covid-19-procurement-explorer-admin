# Generated by Django 3.1.2 on 2021-01-26 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("country", "0018_auto_20210119_1121"),
        ("content", "0023_dataimport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataimport",
            name="country",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="country.country"),
        ),
    ]
