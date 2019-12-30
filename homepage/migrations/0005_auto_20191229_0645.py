# Generated by Django 2.2.9 on 2019-12-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='photo',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('photo', models.ImageField(upload_to='')),
                ('project', models.ForeignKey(null=True, on_delete='SET_NULL', to='homepage.Project')),
            ],
        ),
    ]
