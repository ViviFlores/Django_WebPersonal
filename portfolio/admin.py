from django.contrib import admin
from .models import Project


# configuración extendida al administrador
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Register your models here.
admin.site.register(Project, ProjectAdmin)
