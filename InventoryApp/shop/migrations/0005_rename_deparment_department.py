# Generated by Django 4.0 on 2022-09-06 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_deparment_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deparment',
            new_name='Department',
        ),
    ]