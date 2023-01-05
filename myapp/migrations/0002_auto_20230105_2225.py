# Generated by Django 3.2.16 on 2023-01-05 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso', models.CharField(max_length=3)),
                ('long_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='holding',
            old_name='local_currency_value',
            new_name='value',
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_currency', models.CharField(max_length=3)),
                ('rate', models.FloatField(default=1.0)),
                ('last_update_time', models.DateTimeField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.currency')),
            ],
        ),
        migrations.AlterField(
            model_name='holding',
            name='iso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.currency'),
        ),
    ]