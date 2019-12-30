# Generated by Django 2.2.9 on 2019-12-29 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_auto_20191229_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliodata',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='portfoliodata',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliodata',
            name='firstname',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliodata',
            name='lastname',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliodata',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliodata',
            name='portfolio',
            field=models.FileField(null=True, upload_to='pdf'),
        ),
    ]