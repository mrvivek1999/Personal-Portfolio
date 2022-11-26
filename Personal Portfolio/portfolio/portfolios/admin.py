

from django.contrib import admin

# Register your models here.
from .models import tech, software, Project

admin.site.register(tech)
admin.site.register(software)
admin.site.register(Project)