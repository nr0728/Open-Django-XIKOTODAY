# Generated by Django 5.0.3 on 2024-04-04 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
