# Generated by Django 4.0.5 on 2022-06-20 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='animal',
        ),
    ]