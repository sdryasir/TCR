# Generated by Django 5.0.6 on 2024-08-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Why_Choose_Us_Section', '0003_rename_feature_why_choose_us_section_feature_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='why_choose_us_section',
            name='mobile_background_image',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='Counter_Section/'),
        ),
    ]