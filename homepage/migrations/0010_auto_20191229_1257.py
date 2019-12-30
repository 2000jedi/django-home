# Generated by Django 2.2.9 on 2019-12-29 12:57

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20191229_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='education',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), default='', max_length=1010, size=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeconfig',
            name='photo',
            field=models.ImageField(null=True, upload_to='selfie'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio',
            field=models.FileField(upload_to='pdf'),
        ),
    ]