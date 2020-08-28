# Generated by Django 3.0.9 on 2020-08-28 18:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was modified', verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted at')),
                ('date', models.DateField()),
                ('shift', models.CharField(choices=[('morning', 'morning'), ('afternoon', 'afternoon'), ('evening', 'evening'), ('night', 'night')], default='morning', max_length=10)),
                ('duration', models.TimeField(blank=True, null=True)),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('count_children', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=10, message='The maximum number of children per babysitter must be 10')])),
                ('special_cares', models.CharField(blank=True, help_text='Write the special cares to consider for each child', max_length=255, null=True, verbose_name='Special Cares')),
                ('is_active', models.BooleanField(default=True, verbose_name='Service Active')),
                ('service_start', models.DateTimeField(blank=True, null=True, verbose_name='Datetime service starts')),
                ('service_end', models.DateTimeField(blank=True, null=True, verbose_name='Datetime service ends')),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Total service cost')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
