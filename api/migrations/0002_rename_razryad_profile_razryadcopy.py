# Generated by Django 3.2.7 on 2021-09-19 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='razryad',
            new_name='razryadcopy',
        ),
    ]