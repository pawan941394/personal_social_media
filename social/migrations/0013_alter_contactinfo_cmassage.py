# Generated by Django 3.2 on 2021-04-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_alter_contactinfo_cmassage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='Cmassage',
            field=models.TextField(max_length=5000),
        ),
    ]