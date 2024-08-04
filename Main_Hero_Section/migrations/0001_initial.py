# Generated by Django 5.0.6 on 2024-08-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Hero_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=60)),
                ('price', models.CharField(max_length=60)),
                ('image', models.FileField(max_length=200, null=True, upload_to='Main-Hero-Section/')),
            ],
        ),
    ]
