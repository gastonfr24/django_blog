from django import forms
from .models import post


class postCreateForm(forms.ModelForm):

    class Meta:
        model = post
        fields = ("tittle", 'content')
