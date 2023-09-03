from django.shortcuts import render, redirect
from app.models import Setting, Skill, Project, Tool, ContactForm
from django.contrib.auth.decorators import login_required

def index(request, name=None):
    if(name != None):
        setting = Setting.objects.filter(full_name=name).first()
    else:
        setting = Setting.objects.filter(owner__is_superuser=True).first()
    if(request.method == "POST"):
        if(request.POST['name'] != None and request.POST['name'] != ""):
            if(request.POST['email'] != None and request.POST['email'] != ""):
                if(request.POST['message'] != None and request.POST['message'] != ""):
                    contact_form = ContactForm(setting=setting, name=request.POST['name'], email=request.POST['email'], message=request.POST['message'])
                    contact_form.save()
        return redirect(request.path)
    if(setting):
        skills = Skill.objects.filter(setting=setting)
        projects = Project.objects.filter(setting=setting)
        return render(request, 'index.html', {"setting": setting, "skills": skills, "projects": projects})
    return redirect('notfound')

def project(request, name=None, id=None):
    if(id):
        project = Project.objects.filter(id=id).first()
        if(project  ):
            tools = Tool.objects.filter(project=project)
            return render(request, 'project.html', {"setting": project.setting, "project": project, "tools": tools})
    return redirect('index')

def notfound(request):
    return render(request, 'notfound.html')