# Generated by Django 5.0.6 on 2024-09-17 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsletter', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsletter',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='subscribed_at',
        ),
    ]
