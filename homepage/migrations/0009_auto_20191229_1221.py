# Generated by Django 2.2.9 on 2019-12-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20191229_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconfig',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(),
        ),
    ]
