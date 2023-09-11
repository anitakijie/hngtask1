# Generated by Django 4.2.5 on 2023-09-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(200, 'OK'), (201, 'CREATED'), (400, 'FAILED')], default=200, max_length=20),
        ),
    ]