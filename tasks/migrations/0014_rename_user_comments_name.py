# Generated by Django 5.0.4 on 2024-04-09 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_rename_name_comments_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='name',
        ),
    ]
