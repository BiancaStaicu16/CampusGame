# Generated by Django 3.1.6 on 2022-03-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="score",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
