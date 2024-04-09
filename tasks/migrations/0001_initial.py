# Generated by Django 5.0.4 on 2024-04-04 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MemberDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('img', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('cover', models.URLField()),
                ('duedate', models.DateField(auto_now=True)),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('labels', models.ManyToManyField(related_name='labels', to='tasks.labels')),
                ('members', models.ManyToManyField(related_name='member', to='tasks.memberdetail')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.taskstage')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('src', models.URLField(max_length=250)),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('src', models.URLField(max_length=250)),
                ('size', models.CharField(max_length=200)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]