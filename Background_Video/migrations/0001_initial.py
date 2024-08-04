# Generated by Django 5.0.6 on 2024-08-04 10:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Background_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('title_line_1', models.CharField(max_length=60, null=True)),
                ('title_line_2', models.CharField(max_length=60, null=True)),
                ('description', models.CharField(max_length=60, null=True)),
                ('download_button', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Background Video',
            },
        ),
    ]
