# Generated by Django 5.0.3 on 2024-04-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
