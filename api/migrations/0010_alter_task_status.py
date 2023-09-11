# Generated by Django 4.2.5 on 2023-09-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[('OK', 200), ('CREATED', 201), ('FAILED', 400)], default=200, max_length=20),
        ),
    ]