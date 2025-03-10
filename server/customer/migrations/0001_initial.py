# Generated by Django 4.2.19 on 2025-03-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cc_number', models.CharField(max_length=16)),
                ('cc_expiry_month', models.IntegerField()),
                ('cc_expiry_year', models.IntegerField()),
            ],
        ),
    ]
