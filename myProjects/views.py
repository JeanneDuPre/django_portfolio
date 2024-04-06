from django.shortcuts import render
from . models import *
from django.shortcuts import render, get_object_or_404
import random

def projects(request):
    projects = Projekt.objects.all()
    ctx = {'projects': projects}
    for project in projects: 
        skills = project.skills.split(', ')
        project.skills_list = skills if len(skills) > 1 else [skills[0]]
    return render(request, 'projects.html', ctx)

def project_detail(request, project_id):
    project = get_object_or_404(Projekt, id=project_id)
    # Split the skills and create skills_list attribute
    skills = project.skills.split(', ')
    project.skills_list = skills if len(skills) > 1 else [skills[0]]
    return render(request, 'project_detail.html', {'project': project})

def project_list(request):
    projects = Projekt.objects.all()
    for project in projects:
        skills = project.skills.split(',')
        project.skills_list = skills if len(skills) > 1 else [skills[0]]
    return render(request, 'projects.html', {'projects': projects})

def vita(request):
    return render(request, 'vita.html')

def random_projects(request):
    # Get all projects from your database
    all_projects = list(Projekt.objects.all())
    # Shuffle the list of projects randomly
    random.shuffle(all_projects)
    # Get the first three projects after shuffling
    random_three_projects = all_projects[:3]
    
    # Fetch skills for each project
    for project in random_three_projects:
        project.skills_list = project.skills.split(',')  # Assuming skills is a comma-separated field
        
    # Pass the three random projects to the template
    return render(request, 'home.html', {'random_projects': random_three_projects})

def home(request):
    # Get all projects from your database
    projects = Projekt.objects.all()
    return render(request, 'home.html')

def zukunft(request):
    return render(request, 'zukunft.html')

# Create your views here.
def fehler404(request, exception):
    return render(request, '404.html')