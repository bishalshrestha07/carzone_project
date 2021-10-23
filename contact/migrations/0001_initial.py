# Generated by Django 3.2.6 on 2021-10-22 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('car_id', models.IntegerField()),
                ('customer_need', models.CharField(max_length=100)),
                ('car_title', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
