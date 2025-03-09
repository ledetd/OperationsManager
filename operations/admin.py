from django.contrib import admin
from . models import Operation, Project, ProjectManager

admin.site.register(Operation)
admin.site.register(Project)
admin.site.register(ProjectManager)
