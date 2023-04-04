from django import forms
from app01.models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['subject', 'ctx_text', 'ctx_image']

        widgets = {
            'subject': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'제목',
            }),
            'ctx_text': forms.Textarea(attrs={
                'class':'form-control',
                'rows': 10,
                'placeholder':'내용',
            }),
        }
        labels = {
            'subject': '제목',
            'ctx_text': '내용',
            'ctx_image': '이미지',
        }
