# Generated by Django 4.0.5 on 2022-06-19 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
        ('characteristics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristics',
            name='animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='animals.animal'),
        ),
    ]