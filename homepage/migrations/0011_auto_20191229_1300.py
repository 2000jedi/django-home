# Generated by Django 2.2.9 on 2019-12-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_auto_20191229_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='education',
            field=models.TextField(),
        ),
    ]