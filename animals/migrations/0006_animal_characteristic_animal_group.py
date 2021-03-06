# Generated by Django 4.0.5 on 2022-06-21 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_remove_group_animal'),
        ('characteristics', '0010_remove_characteristics_animal'),
        ('animals', '0005_remove_animal_characteristics'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='characteristic',
            field=models.ManyToManyField(related_name='animal', to='characteristics.characteristics'),
        ),
        migrations.AddField(
            model_name='animal',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='groups.group'),
        ),
    ]
