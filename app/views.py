from django.shortcuts import get_object_or_404, render

from .models import Project


def home(request):
    return render(request, "home.html")


def about_us(request):
    return render(request, "about_us.html")


def services(request):
    return render(request, "services.html")


def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio.html", {"projects": projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "project_detail.html", {"project": project})


def portfolio_view(request):
    projects = Project.objects.all()
    return render(request, "portfolio.html", {"projects": projects})
