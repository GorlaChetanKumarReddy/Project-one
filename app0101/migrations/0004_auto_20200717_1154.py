# Generated by Django 3.0.8 on 2020-07-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0101', '0003_user_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_shedule_class_model',
            name='date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='new_shedule_class_model',
            name='time',
            field=models.TimeField(max_length=100),
        ),
    ]
