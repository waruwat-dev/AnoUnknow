# Generated by Django 3.0.5 on 2020-04-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_auto_20200418_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcementmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]