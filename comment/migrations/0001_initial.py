# Generated by Django 4.2.2 on 2023-06-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=20)),
                ('book_id', models.CharField(max_length=20)),
                ('rate', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
    ]
