# Generated by Django 4.2.3 on 2023-07-28 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_membersmodel_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileModel',
        ),
    ]