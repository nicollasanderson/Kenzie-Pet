# Generated by Django 4.0.5 on 2022-06-20 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_remove_animal_group'),
        ('groups', '0003_remove_group_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal', to='animals.animal'),
        ),
    ]
