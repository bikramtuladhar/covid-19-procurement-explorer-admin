# Generated by Django 3.1.2 on 2020-11-26 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("population", models.BigIntegerField(null=True, verbose_name="Population")),
                ("gdp", models.FloatField(null=True, verbose_name="GDP")),
                ("country_code", models.CharField(max_length=10, null=True, verbose_name="Country code")),
                ("currency", models.CharField(max_length=50, null=True, verbose_name="Currency")),
                ("healthcare_budget", models.FloatField(null=True, verbose_name="Healthcare budget")),
                ("healthcare_gdp_pc", models.FloatField(null=True, verbose_name="% of GDP to healthcare")),
                ("covid_cases_total", models.IntegerField(null=True, verbose_name="Total COVID-19 cases")),
                ("covid_deaths_total", models.IntegerField(null=True, verbose_name="Total deaths by Covid-19")),
                ("covid_data_last_updated", models.DateTimeField(null=True)),
                ("equity_unemployment_rate", models.FloatField(null=True, verbose_name="Unemployment rate")),
                ("equity_income_avg", models.FloatField(null=True, verbose_name="Average income")),
                ("equity_gender_dist_male", models.FloatField(null=True, verbose_name="Gender distribution male")),
                ("equity_gender_dist_female", models.FloatField(null=True, verbose_name="Gender distribution female")),
                ("equity_age_dist_0_14", models.FloatField(null=True, verbose_name="Age distribution 0-14 years")),
                ("equity_age_dist_15_24", models.FloatField(null=True, verbose_name="Age distribution 15-24 years")),
                ("equity_age_dist_25_54", models.FloatField(null=True, verbose_name="Age distribution 25-54 years")),
                ("equity_age_dist_55_64", models.FloatField(null=True, verbose_name="Age distribution 55-64 years")),
                (
                    "equity_age_dist_65_above",
                    models.FloatField(null=True, verbose_name="Age distribution 55-above years"),
                ),
                (
                    "procurement_annual_public_spending",
                    models.FloatField(null=True, verbose_name="Annual public procurement spending"),
                ),
                ("procurement_gdp_pc", models.FloatField(null=True, verbose_name="% of Procurement to GDP")),
                ("procurement_covid_spending", models.FloatField(null=True, verbose_name="COVID-19 spending")),
                (
                    "procurement_total_market_pc",
                    models.FloatField(null=True, verbose_name="% from total procurement market"),
                ),
                (
                    "covid19_procurement_policy",
                    models.TextField(null=True, verbose_name="COVID-19 Procurement Policy"),
                ),
                ("covid19_preparedness", models.TextField(null=True, verbose_name="COVID-19 Preparedness")),
            ],
            options={
                "verbose_name_plural": "Countries",
            },
        ),
        migrations.CreateModel(
            name="CurrencyConversionCache",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("source_currency", models.CharField(max_length=50, null=True, verbose_name="Source currency")),
                ("dst_currency", models.CharField(max_length=50, null=True, verbose_name="Dst currency")),
                ("conversion_date", models.DateField(null=True, verbose_name="Conversion date")),
                ("conversion_rate", models.FloatField(null=True, verbose_name="Conversion rate")),
            ],
        ),
        migrations.CreateModel(
            name="Language",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("code", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("supplier_id", models.CharField(max_length=50, null=True, unique=True, verbose_name="Supplier ID")),
                ("supplier_name", models.CharField(max_length=250, verbose_name="Supplier name")),
            ],
        ),
        migrations.CreateModel(
            name="Tender",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("contract_id", models.CharField(max_length=50, null=True, verbose_name="Contract ID")),
                ("contract_date", models.DateField(null=True, verbose_name="Contract date")),
                ("contract_title", models.TextField(null=True, verbose_name="Contract title")),
                ("contract_value_local", models.FloatField(null=True, verbose_name="Contract value local")),
                ("contract_value_usd", models.FloatField(null=True, verbose_name="Contract value USD")),
                ("contract_desc", models.TextField(null=True, verbose_name="Contract description")),
                (
                    "procurement_procedure",
                    models.CharField(
                        choices=[
                            ("open", "open"),
                            ("limited", "limited"),
                            ("direct", "direct"),
                            ("selective", "selective"),
                        ],
                        max_length=25,
                        null=True,
                        verbose_name="Procurement procedure",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "active"), ("completed", "completed"), ("canceled", "canceled")],
                        max_length=25,
                        null=True,
                        verbose_name="Contract status",
                    ),
                ),
                ("link_to_contract", models.CharField(max_length=250, null=True, verbose_name="Link to contract")),
                ("link_to_tender", models.CharField(max_length=250, null=True, verbose_name="Link to tender")),
                ("data_source", models.CharField(max_length=250, null=True, verbose_name="Data source")),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="tenders", to="country.country"
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="suppliers", to="country.supplier"
                    ),
                ),
            ],
        ),
    ]
