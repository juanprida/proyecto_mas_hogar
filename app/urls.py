from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-nosotros/', views.about_us, name='about_us'),
    path('servicios/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
]
