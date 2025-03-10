# Generated by Django 5.1.7 on 2025-03-09 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0002_projectmanager_project'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('well_name', models.CharField(max_length=100)),
                ('project_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='operations.project')),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectDetail',
        ),
    ]
