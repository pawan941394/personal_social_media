# Generated by Django 3.2 on 2021-04-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_alter_contactinfo_cmassage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='Cmassage',
            field=models.CharField(max_length=5000),
        ),
    ]
