# Generated by Django 3.1.6 on 2022-03-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, unique=True)),
                ("value", models.DecimalField(decimal_places=2, max_digits=19)),
                ("picture", models.FileField(blank=True, null=True, upload_to="")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
