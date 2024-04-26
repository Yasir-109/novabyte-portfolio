from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
    
def projects(request):
    projects = Project.objects.all()  # Assuming Project is the model for projects
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio/project.html', {'project': project})