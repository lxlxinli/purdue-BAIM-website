# Generated by Django 3.0.4 on 2020-05-22 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0027_achievements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='achievements',
            new_name='achievement',
        ),
    ]