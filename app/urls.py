from django.contrib import admin
from django.urls import path
from app.views import index, notfound, project

urlpatterns = [
    path('site/<str:name>', index, name="index"),
    path('', index, name="index"),
    path('project/<int:id>', project, name="project"),
    path('<str:name>/project/<int:id>', project, name="project"),
    path('notfound/', notfound, name='notfound'),
]
