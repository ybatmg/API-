# Generated by Django 5.0.4 on 2024-04-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachments',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='attachments',
            field=models.ManyToManyField(null=True, to='tasks.attachments'),
        ),
    ]
