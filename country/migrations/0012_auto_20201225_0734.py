# Generated by Django 3.1.2 on 2020-12-25 07:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0011_country_continent'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, null=True, unique=True, verbose_name='Category name')),
            ],
        ),
        migrations.AddField(
            model_name='tender',
            name='equity_categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10, null=True), default=list, null=True, size=None),
        ),
        migrations.CreateModel(
            name='EquityKeywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=50, verbose_name='Keyword')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equity_keywords', to='country.country')),
                ('equity_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equity_keywords', to='country.equitycategory')),
            ],
        ),
    ]
