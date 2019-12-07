# Generated by Django 3.0 on 2019-12-07 05:19

import datetime

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schedule",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="", max_length=128)),
                ("start", models.DateTimeField(default=django.utils.timezone.now)),
                ("finish", models.DateTimeField(default=None, null=True)),
                ("every", models.DurationField(default=datetime.timedelta(seconds=3600))),
            ],
        ),
    ]
