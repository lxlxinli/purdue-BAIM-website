# Generated by Django 3.0.3 on 2020-03-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('ID', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=50)),
                ('purdue_email', models.CharField(max_length=120)),
                ('linkedin', models.URLField()),
                ('analytics_experience', models.IntegerField()),
                ('total_professional_experience', models.IntegerField()),
                ('data_analyst', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('business_analyst', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('data_scientist', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('consultant', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('developer', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('within_US', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('international', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('mid_atlantic', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('midwest', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('northeast', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('pacific_northwest', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('south', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('southeast', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('southwest', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
                ('west', models.IntegerField(choices=[(None, ''), (0, 'No'), (1, 'Yes')], max_length=1)),
            ],
        ),
    ]
