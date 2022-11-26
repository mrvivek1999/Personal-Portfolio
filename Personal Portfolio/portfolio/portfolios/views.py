

from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import *
from .forms import *
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse

def index(request):
    ctx = {}
    ctx['title'] = 'Home'
    ctx['project'] = Project
    return render(request, 'project/index.html', ctx)

def project_create(request):
    ctx = {'title': 'Create Project | Portfolio'}
    project_form = ProjectForm(request.POST , request.FILES )
    tech_form = TechForm()
    software_form = SoftwareForm()
    if project_form.is_valid():
        project = project_form.save(commit=False) # save the form partially
        project.save()
        messages.success(request, 'Project created successfully')  

    ctx['project_form'] = project_form
    ctx['tech_form'] = tech_form
    ctx['software_form'] = software_form
    return render(request, 'project/project_create.html', ctx)

def tech_create(request):
    if request.method == 'POST':
        tech_form = TechForm(request.POST)
        if tech_form.is_valid():
            tech = tech_form.save(commit=False)
            tech.save()
            return JsonResponse({'status': 'success', 'name': tech.name, 'id': tech.id})
        else:
            return JsonResponse({'status': 'invalid data'})
    else:
        return JsonResponse({'status': 'error'})

def software_create(request):
    if request.method == 'POST':
        software_form = SoftwareForm(request.POST)
        if software_form.is_valid():
            software = software_form.save(commit=False)
            software.save()
            return JsonResponse({'status': 'success', 'name': software.name, 'id': software.id})
        else:
            return JsonResponse({'status': 'invalid data'})
    else:
        return JsonResponse({'status': 'error'})



