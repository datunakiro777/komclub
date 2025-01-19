# Generated by Django 5.1.4 on 2025-01-18 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0011_comments_club_alter_comments_create_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='club',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='club_comments', to='clubs.clubs_info'),
        ),
    ]