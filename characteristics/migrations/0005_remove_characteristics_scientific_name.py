# Generated by Django 4.0.5 on 2022-06-20 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characteristics', '0004_characteristics_scientific_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characteristics',
            name='scientific_name',
        ),
    ]