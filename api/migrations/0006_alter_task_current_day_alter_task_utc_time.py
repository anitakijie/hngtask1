# Generated by Django 4.2.5 on 2023-09-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_task_current_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='current_day',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='utc_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]