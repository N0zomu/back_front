# Generated by Django 4.2.2 on 2023-06-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='chaper_id',
        ),
        migrations.AddField(
            model_name='chapter',
            name='chapter_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chapter',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='book_id',
            field=models.IntegerField(default=0),
        ),
    ]