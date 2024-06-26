# Generated by Django 5.0.2 on 2024-04-23 16:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=800)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(default='https://www.svgrepo.com/show/192244/man-user.svg', max_length=800)),
                ('age', models.IntegerField(default=0)),
                ('first_name', models.CharField(max_length=800)),
                ('last_name', models.CharField(max_length=800)),
                ('father_name', models.CharField(max_length=800)),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('W', 'Работник'), ('B', 'Руководитель')], default='W', max_length=800)),
                ('job_title_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='essential.jobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=800)),
                ('hoursToAccomplish', models.IntegerField(default=0)),
                ('stageAt', models.CharField(choices=[('G', 'Готово'), ('R', 'В процессе'), ('O', 'В обсуждении')], default='O', max_length=20)),
                ('priority', models.IntegerField(default=0)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='essential.project')),
                ('workers', models.ManyToManyField(to='essential.user')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(to='essential.user'),
        ),
        migrations.CreateModel(
            name='UserProjectsAndTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essential.user')),
            ],
        ),
    ]
