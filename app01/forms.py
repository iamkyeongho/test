from django import forms
from app01.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['subject', 'ctx_text', 'ctx_image']
