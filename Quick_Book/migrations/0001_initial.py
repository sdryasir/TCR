# Generated by Django 5.0.6 on 2024-09-08 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quick_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('car', models.CharField(max_length=60)),
                ('pickupdate', models.DateField()),
                ('returndate', models.DateField()),
            ],
        ),
    ]