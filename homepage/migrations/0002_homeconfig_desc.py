# Generated by Django 2.2.9 on 2019-12-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconfig',
            name='desc',
            field=models.TextField(default='placeholder'),
            preserve_default=False,
        ),
    ]