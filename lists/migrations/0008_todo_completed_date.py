# Generated by Django 2.0.2 on 2018-02-16 03:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0007_todo_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]