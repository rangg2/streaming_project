# Generated by Django 4.2.6 on 2023-10-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime_info',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='anime_info',
            name='airday',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='anime_info',
            name='genres',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='anime_info',
            name='production',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='anime_info',
            name='tags',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='anime_info',
            name='viewable',
            field=models.BooleanField(default='1'),
        ),
        migrations.AlterField(
            model_name='anime_info',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
