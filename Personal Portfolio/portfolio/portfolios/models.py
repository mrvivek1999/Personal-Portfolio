from django.db import models

from django.conf import settings


# pip install `django-tinymce` for the import below
from tinymce.models import HTMLField

class tech(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class software(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    tech = models.ManyToManyField(tech)
    software = models.ManyToManyField(software)
    image = models.ImageField(upload_to="images/" , null=True)
    video = models.FileField()
   


    def __str__(self):
        return self.title


   
    

# Create your models here.
