# Generated by Django 3.0.4 on 2020-05-22 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0026_auto_20200517_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_name', models.CharField(default='', max_length=500)),
                ('posterlink', models.CharField(default='', max_length=500)),
                ('conference', models.CharField(default='', max_length=100)),
                ('comments', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
