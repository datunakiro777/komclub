# Generated by Django 5.0.3 on 2025-01-02 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_info_options_alter_user_info_managers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='username',
            new_name='name',
        ),
    ]
