# Generated by Django 5.0.3 on 2024-05-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_dream_profile_dream_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dream',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
