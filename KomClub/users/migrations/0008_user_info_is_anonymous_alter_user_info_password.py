# Generated by Django 5.0.3 on 2025-01-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_info_options_alter_user_info_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
