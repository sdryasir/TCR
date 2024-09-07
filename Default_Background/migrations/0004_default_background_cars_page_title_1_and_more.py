# Generated by Django 5.0.6 on 2024-09-02 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Default_Background', '0003_alter_default_background_about_page_title_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='default_background',
            name='Cars_Page_Title_1',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Cars_Page_Title_2',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Cars_Page_description_1',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Cars_Page_description_2',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Team_Page_Title_1',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Team_Page_Title_2',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Team_Page_description_1',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Team_Page_description_2',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
