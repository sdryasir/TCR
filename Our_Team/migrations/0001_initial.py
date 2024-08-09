# Generated by Django 5.0.6 on 2024-08-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Our_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('profession', models.CharField(max_length=60)),
                ('facebook_link', models.TextField(blank=True, max_length=300, null=True)),
                ('twitter_link', models.TextField(blank=True, max_length=300, null=True)),
                ('instagram_link', models.TextField(blank=True, max_length=300, null=True)),
                ('image', models.FileField(max_length=200, null=True, upload_to='Our_Team/')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Team Cards',
            },
        ),
    ]
