# Generated by Django 4.1.7 on 2023-03-03 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomA", models.CharField(max_length=100)),
                ("age", models.IntegerField(default=0)),
                ("calandrier", models.DateField()),
            ],
        ),
    ]
