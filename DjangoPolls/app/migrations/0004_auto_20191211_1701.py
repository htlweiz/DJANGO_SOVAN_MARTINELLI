# Generated by Django 2.2.8 on 2019-12-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191211_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='geplanter_status',
            field=models.BooleanField(verbose_name='geplanter_status'),
        ),
    ]
