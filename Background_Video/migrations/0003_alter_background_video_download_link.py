# Generated by Django 5.0.6 on 2024-09-02 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Background_Video', '0002_background_video_download_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background_video',
            name='download_link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]