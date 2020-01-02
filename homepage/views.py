from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def index(request):
    homeConfig = models.HomeConfig.objects.all()[0]
    projects = models.Project.objects.filter(showcase__gt = 0)

    mod = {
        'server' : homeConfig.server,
        'title'  : homeConfig.title,
        'desc'   : homeConfig.desc,
        'url'    : homeConfig.serv_url,
        'selfie' : homeConfig.photo,
        'projs'  : projects,
    }

    return render(request, 'index.html', mod)

def project_home(request):
    homeConfig = models.HomeConfig.objects.all()[0]
    projects = models.Project.objects.order_by('-date')

    mod = {
        'server' : homeConfig.server,
        'title'  : homeConfig.title,
        'desc'   : homeConfig.desc,
        'url'    : homeConfig.serv_url,
        'projs'  : projects,
    }


    return render(request, 'project.html', mod)

def portfolio_preview(request):
    homeConfig = models.HomeConfig.objects.all()[0]
    info       = models.PortfolioData.objects.all()[0]
    ps = models.Portfolio.objects.all()

    mod = {
        'server' : homeConfig.server,
        'title'  : homeConfig.title,
        'desc'   : homeConfig.desc,
        'url'    : homeConfig.serv_url,
        'info'   : info,
        'states' : ps,
    }

    return render(request, 'portfolio.html', mod)
