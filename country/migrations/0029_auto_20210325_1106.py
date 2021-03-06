# Generated by Django 3.1.2 on 2021-03-25 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("country", "0028_tender_temp_table_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="goodsservices",
            name="ppu_including_vat",
            field=models.CharField(max_length=1500, null=True, verbose_name="Price per units including VAT"),
        ),
        migrations.AddField(
            model_name="goodsservices",
            name="quantity_units",
            field=models.CharField(max_length=1500, null=True, verbose_name="Quantity,units"),
        ),
    ]
