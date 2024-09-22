# Generated by Django 5.0.6 on 2024-09-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Default_Background', '0005_default_background_faq_page_title_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='default_background',
            name='Blog_Page_Title_1',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Blog_Page_Title_2',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Blog_Page_description_1',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='default_background',
            name='Blog_Page_description_2',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
