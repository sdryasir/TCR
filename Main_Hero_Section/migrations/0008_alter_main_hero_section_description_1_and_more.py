# Generated by Django 5.0.6 on 2024-08-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Hero_Section', '0007_rename_description_main_hero_section_description_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_hero_section',
            name='description_1',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='main_hero_section',
            name='description_2',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='main_hero_section',
            name='image',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='Main_Hero_Section/'),
        ),
        migrations.AlterField(
            model_name='main_hero_section',
            name='price',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='main_hero_section',
            name='title_1',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='main_hero_section',
            name='title_2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]