# Generated by Django 5.0.6 on 2024-08-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=60, null=True)),
                ('image', models.FileField(max_length=200, null=True, upload_to='Testimonial/')),
                ('name', models.CharField(max_length=60, null=True)),
                ('post', models.CharField(max_length=60, null=True)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Testimonial',
            },
        ),
    ]