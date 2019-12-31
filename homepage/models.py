from django.db import models
from django.contrib import admin

from markdownx.models import MarkdownxField
from markdownx.admin  import MarkdownxModelAdmin
from markdownx.utils  import markdownify

# Create your models here.

class HomeConfig(models.Model):
    server   = models.CharField(max_length=100)
    title    = models.CharField(max_length=100)
    serv_url = models.CharField(max_length=100, default='my server')
    desc     = models.TextField()
    photo    = models.ImageField(null=True, blank=True, upload_to='selfie')

class Project(models.Model):
    title      = models.CharField(max_length=100, primary_key=True, unique=True)
    short_desc = models.CharField(max_length=255, blank=True)
    long_desc  = MarkdownxField()
    github_url = models.URLField(null=True)
    showcase   = models.IntegerField(default=-1)
    date       = models.DateField()

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.long_desc)

class Photo(models.Model):
    name    = models.CharField(max_length=100, primary_key=True, unique=True)
    photo   = models.ImageField(upload_to='photos')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)

class PortfolioData(models.Model):
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    email     = models.EmailField()
    address   = models.CharField(max_length=255, null=True, blank=True)
    phone     = models.CharField(max_length=20, null=True, blank=True)
    footage   = models.TextField(null=True, blank=True)
    pdf = models.FileField(name='portfolio', upload_to='pdf', null=True, blank=True)

class Portfolio(models.Model):
    choices = (
        ('E', 'education'),
        ('A', 'award'),
        ('P', 'project')
    )
    choice = models.CharField(
        max_length=1,
        choices=choices,
        default='E',
    )
    name       = models.CharField(max_length=100)
    date_begin = models.DateField()
    date_end   = models.DateField()
    desc       = models.TextField(blank=True)

    def __str__(self):
        return self.choice + ': ' + self.name

admin.site.register(HomeConfig)
admin.site.register(Photo)
admin.site.register(Project, MarkdownxModelAdmin)
admin.site.register(Portfolio)
admin.site.register(PortfolioData)
