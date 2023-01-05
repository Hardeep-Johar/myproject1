# Generated by Django 3.2.16 on 2023-01-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso', models.CharField(max_length=3)),
                ('local_currency_value', models.FloatField(default=0.0)),
                ('buy_date', models.DateField()),
            ],
        ),
    ]
