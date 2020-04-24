# Generated by Django 3.0.3 on 2020-04-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_announcementmodel_adminid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcementmodel',
            name='type',
            field=models.CharField(choices=[('02', 'Warning'), ('01', 'Normal')], default='01', max_length=2),
        ),
    ]