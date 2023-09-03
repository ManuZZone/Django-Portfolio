from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest
from app.models import Setting, Skill, Project, ContactForm, Tool
from django.contrib.auth.models import User

class SettingAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if(request.user.is_superuser):
            return queryset
        return queryset.filter(owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "owner" and not request.user.is_superuser:
            kwargs["queryset"] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, *args, **kwargs):
        form = super(SettingAdmin, self).get_form(request, *args, **kwargs)
        form.base_fields['owner'].initial = request.user
        return form

class SkillAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if(request.user.is_superuser):
            return queryset
        return queryset.filter(setting__owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "setting" and not request.user.is_superuser:
            kwargs["queryset"] = Setting.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class ProjectAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if(request.user.is_superuser):
            return queryset
        return queryset.filter(setting__owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "setting" and not request.user.is_superuser:
            kwargs["queryset"] = Setting.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs) 

class ContactFormAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if(request.user.is_superuser):
            return queryset
        return queryset.filter(setting__owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "setting" and not request.user.is_superuser:
            kwargs["queryset"] = Setting.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs) 

class ToolAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if(request.user.is_superuser):
            return queryset
        return queryset.filter(project__setting__owner=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "project" and not request.user.is_superuser:
            kwargs["queryset"] = Project.objects.filter(setting__owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs) 

admin.site.register(Setting, SettingAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Tool, ToolAdmin)
