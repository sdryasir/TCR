# Generated by Django 5.0.6 on 2024-08-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('tag', models.CharField(max_length=20, null=True)),
                ('image', models.FileField(max_length=200, null=True, upload_to='Blog/')),
                ('Blog_details_heading_1', models.CharField(blank=True, max_length=150, null=True)),
                ('Blog_details_description_1', models.CharField(blank=True, max_length=700, null=True)),
                ('Blog_details_description_2', models.CharField(blank=True, max_length=700, null=True)),
                ('Blog_details_heading_2', models.CharField(blank=True, max_length=150, null=True)),
                ('Blog_details_heading_2_description', models.CharField(blank=True, max_length=700, null=True)),
                ('feature_1', models.CharField(blank=True, max_length=150, null=True)),
                ('feature_2', models.CharField(blank=True, max_length=150, null=True)),
                ('feature_3', models.CharField(blank=True, max_length=150, null=True)),
                ('blog_details_image', models.FileField(blank=True, max_length=200, null=True, upload_to='Blog/')),
                ('tips_heading', models.CharField(blank=True, max_length=150, null=True)),
                ('tips_description', models.CharField(blank=True, max_length=700, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]