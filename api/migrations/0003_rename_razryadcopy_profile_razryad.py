# Generated by Django 3.2.7 on 2021-09-19 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_razryad_profile_razryadcopy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='razryadcopy',
            new_name='razryad',
        ),
    ]
