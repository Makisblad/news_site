from django import forms
import re
from .models import *
from django.core.exceptions import ValidationError

class NewsForm (forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'categories': forms.Select(attrs={'class': 'form-control'}),

        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно зачинаться с цифры')
        return title


        #fields = '__all__'