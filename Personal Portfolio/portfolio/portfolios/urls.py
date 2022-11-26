


from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='home'),
    path('project/new/', project_create, name='project_create'),
    path('api/tech/create/', tech_create, name='tech_create'),
    path('api/software/create/', software_create, name='software_create'),
  ]