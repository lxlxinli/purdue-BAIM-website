# Generated by Django 3.0.4 on 2020-05-15 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0023_auto_20200512_0055'),
    ]

    operations = [
        migrations.DeleteModel(
            name='papers',
        ),
        migrations.DeleteModel(
            name='posters',
        ),
    ]