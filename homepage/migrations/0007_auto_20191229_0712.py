# Generated by Django 2.2.9 on 2019-12-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20191229_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='showcase',
            field=models.IntegerField(default=-1),
        ),
    ]