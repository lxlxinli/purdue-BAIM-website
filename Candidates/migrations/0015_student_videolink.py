# Generated by Django 3.0.4 on 2020-04-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidates', '0014_student_picturelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='videolink',
            field=models.URLField(default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAElBMVEUAAADa18308+/p6enp5+H+/v8MLkg4AAABFElEQVR4nO3PCQ3DMAAAsTQPf8prNRQX2Qw8ntuNZ8+b7Xc4z7rXmd9wjXstwzzDPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+wz7DPsM+w77/8Kx7nW+45832O7zdD0WeFNEoVrT6AAAAAElFTkSuQmCC'),
        ),
    ]
