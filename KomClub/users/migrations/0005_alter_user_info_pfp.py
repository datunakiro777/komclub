# Generated by Django 5.1.4 on 2024-12-31 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_info_pfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='pfp',
            field=models.ImageField(default='deafult.jpg', upload_to=''),
        ),
    ]
