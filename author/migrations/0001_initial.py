# Generated by Django 4.2.2 on 2023-06-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("introduction", models.CharField(max_length=500)),
            ],
        ),
    ]
