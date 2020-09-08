# Generated by Django 3.0.9 on 2020-09-07 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='service_origin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_origin', to='services.Service', verbose_name='Client review'),
        ),
    ]
