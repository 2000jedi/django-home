from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_home, name='projects'),
    path('portfolio/', views.portfolio_preview, name='portfolio'),
]
