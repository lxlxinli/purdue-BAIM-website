# Generated by Django 3.0.4 on 2020-05-17 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0024_auto_20200515_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='videolink',
            field=models.URLField(default=''),
        ),
    ]
