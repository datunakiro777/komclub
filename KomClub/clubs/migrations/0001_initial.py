# Generated by Django 5.0.3 on 2024-12-31 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_alter_user_info_last_name_alter_user_info_pfp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('members', models.ManyToManyField(blank=True, null=True, related_name='clubs', to='users.user_info')),
            ],
        ),
    ]
