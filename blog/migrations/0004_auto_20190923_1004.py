# Generated by Django 2.2.5 on 2019-09-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190923_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
    ]
