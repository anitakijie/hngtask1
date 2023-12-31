# Generated by Django 4.2.5 on 2023-09-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(max_length=100)),
                ('track', models.CharField(max_length=100)),
                ('github_file_url', models.URLField()),
                ('github_repo_url', models.URLField()),
            ],
        ),
    ]
