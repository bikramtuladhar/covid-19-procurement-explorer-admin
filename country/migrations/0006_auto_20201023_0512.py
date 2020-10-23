# Generated by Django 3.1.2 on 2020-10-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0005_auto_20201023_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='covid19_preparedness',
            field=models.TextField(null=True, verbose_name='COVID-19 Preparedness'),
        ),
        migrations.AddField(
            model_name='country',
            name='covid19_procurement_policy',
            field=models.TextField(null=True, verbose_name='COVID-19 Procurement Policy'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_age_dist_0_14',
            field=models.FloatField(null=True, verbose_name='Age distribution 0-14 years'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_age_dist_15_24',
            field=models.FloatField(null=True, verbose_name='Age distribution 15-24 years'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_age_dist_25_54',
            field=models.FloatField(null=True, verbose_name='Age distribution 25-54 years'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_age_dist_55_64',
            field=models.FloatField(null=True, verbose_name='Age distribution 55-64 years'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_age_dist_65_above',
            field=models.FloatField(null=True, verbose_name='Age distribution 55-above years'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_gender_dist_female',
            field=models.FloatField(null=True, verbose_name='Gender distribution female'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_gender_dist_male',
            field=models.FloatField(null=True, verbose_name='Gender distribution male'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_income_avg',
            field=models.FloatField(null=True, verbose_name='Average income'),
        ),
        migrations.AddField(
            model_name='country',
            name='equity_unemployment_rate',
            field=models.FloatField(null=True, verbose_name='Unemployment rate'),
        ),
        migrations.AddField(
            model_name='country',
            name='procurement_annual_public_spending',
            field=models.FloatField(null=True, verbose_name='Annual public procurement spending'),
        ),
        migrations.AddField(
            model_name='country',
            name='procurement_covid_spending',
            field=models.FloatField(null=True, verbose_name='COVID-19 spending'),
        ),
        migrations.AddField(
            model_name='country',
            name='procurement_gdp_pc',
            field=models.FloatField(null=True, verbose_name='% of Procurement to GDP'),
        ),
        migrations.AddField(
            model_name='country',
            name='procurement_total_market_pc',
            field=models.FloatField(null=True, verbose_name='% from total procurement market'),
        ),
    ]
