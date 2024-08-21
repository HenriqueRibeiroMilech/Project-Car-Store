# Generated by Django 5.1 on 2024-08-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_mode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mode',
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
