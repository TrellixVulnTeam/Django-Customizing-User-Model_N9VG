# Generated by Django 2.2.5 on 2019-09-23 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190923_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_on',
        ),
    ]
