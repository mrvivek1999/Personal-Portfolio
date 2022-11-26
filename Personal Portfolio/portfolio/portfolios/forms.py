from django import forms
from .models import tech, Project,software
from tinymce.widgets import TinyMCE

class TechForm(forms.ModelForm):
    class Meta:
        model = tech
        fields = ('name',)

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = software
        fields = ('name',)


class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20},))
    tech = forms.ModelMultipleChoiceField(queryset=tech.objects.all(), widget=forms.CheckboxSelectMultiple)
    software = forms.ModelMultipleChoiceField(queryset=software.objects.all(), widget=forms.CheckboxSelectMultiple)
    image = forms.ImageField()
    video = forms.FileField()

    class Meta:
        model = Project
        fields = ('title','description','tech','software','image','video')


        