# Generated by Django 3.0.4 on 2020-05-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0022_papers_posters'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='YEAR2020',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posters',
            name='YEAR2020',
            field=models.IntegerField(default=0),
        ),
    ]
