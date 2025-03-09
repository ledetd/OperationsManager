# Generated by Django 5.1.7 on 2025-03-09 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operations', '0002_projectmanager_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('project_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='operations.project')),
            ],
            bases=('operations.project',),
        ),
    ]
