# Generated by Django 4.2.15 on 2024-08-19 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='std_id',
            field=models.CharField(max_length=5),
        ),
    ]
