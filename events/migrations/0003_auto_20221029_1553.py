# Generated by Django 3.2.16 on 2022-10-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20221009_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='add_information',
            field=models.TextField(default='a', verbose_name='Дополнительное описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='theme',
            field=models.TextField(default='standart', verbose_name='Тема'),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TextField(default='a', verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.TextField(default='a', verbose_name='Дата'),
        ),
    ]
