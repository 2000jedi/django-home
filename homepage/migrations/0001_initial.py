# Generated by Django 3.0.1 on 2019-12-30 11:43

from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('serv_url', models.CharField(default='my server', max_length=100)),
                ('desc', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to='selfie')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('E', 'education'), ('A', 'award'), ('P', 'project')], default='E', max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('desc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('footage', models.TextField(blank=True, null=True)),
                ('portfolio', models.FileField(blank=True, null=True, upload_to='pdf')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('short_desc', models.CharField(blank=True, max_length=255)),
                ('long_desc', markdownx.models.MarkdownxField()),
                ('github_url', models.URLField(null=True)),
                ('showcase', models.IntegerField(default=-1)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('photo', models.ImageField(upload_to='photos')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homepage.Project')),
            ],
        ),
    ]