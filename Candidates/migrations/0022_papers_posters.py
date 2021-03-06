# Generated by Django 3.0.4 on 2020-05-12 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0021_student_videolink'),
    ]

    operations = [
        migrations.CreateModel(
            name='papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Venue', models.CharField(max_length=100, unique=True)),
                ('YEAR2017', models.IntegerField(default=0)),
                ('YEAR2018', models.IntegerField(default=0)),
                ('YEAR2019', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='posters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Venue', models.CharField(max_length=100, unique=True)),
                ('YEAR2017', models.IntegerField(default=0)),
                ('YEAR2018', models.IntegerField(default=0)),
                ('YEAR2019', models.IntegerField(default=0)),
            ],
        ),
    ]
