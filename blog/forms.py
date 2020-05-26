from django import forms

from .models import Post, Cv

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CvForm(forms.ModelForm):

    class Meta:
        model = Cv
        fields = ('header', 'education', 'experience', 'skills_interests', 'awards')
