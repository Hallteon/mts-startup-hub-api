# Generated by Django 3.2.9 on 2022-10-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221008_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
