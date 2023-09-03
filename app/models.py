from django.db import models
from django.contrib.auth.models import User

class Setting(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=32, unique=True)
    hero_description = models.CharField(max_length=256)
    image = models.ImageField()
    about = models.CharField(max_length=512)
    kwown_me = models.CharField(max_length=512)
    project_description = models.CharField(max_length=512)
    contact_description = models.CharField(max_length=512)
    footer_description = models.CharField(max_length=256)
    copyright = models.CharField(max_length=128)
    linkedin_url = models.TextField(blank=True,null=True)
    github_url = models.TextField(blank=True,null=True)
    twitter_url = models.TextField(blank=True,null=True)
    youtube_url = models.TextField(blank=True,null=True)
    instagram_url = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.full_name

class Skill(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    tag = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.setting.full_name + " - " + self.tag

class Project(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    short_description = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    image = models.ImageField()
    url = models.TextField(blank=True,null=True)
    code_url = models.TextField(blank=True,null=True)

    def __str__(self) -> str:
        return self.setting.full_name + " - " + self.name

class Tool(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.project.setting.full_name + " - " + self.project.name + " - " + self.tag

class ContactForm(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    message = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.setting.full_name + " - " + self.email