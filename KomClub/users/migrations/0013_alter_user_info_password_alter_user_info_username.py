# Generated by Django 5.1.4 on 2025-01-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_user_info_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='password',
            field=models.CharField(default='bot123', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='username',
            field=models.CharField(default='bot', max_length=15),
        ),
    ]
