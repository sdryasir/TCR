# Generated by Django 5.0.6 on 2024-08-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Hero_Section', '0006_alter_main_hero_section_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main_hero_section',
            old_name='description',
            new_name='description_1',
        ),
        migrations.AddField(
            model_name='main_hero_section',
            name='car_option',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='main_hero_section',
            name='description_2',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
