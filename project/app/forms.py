from tkinter import Widget
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label="Esimi", widget=forms.TextInput(attrs={'class':'form-input'}))
#     slug = forms.SlugField(max_length=255,label="URL")
#     is_published = forms.BooleanField(label="Kelisim",required=False, initial=True)

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Reg
        fields="__all__"
        # fields=['','']
        widgets={
            'esim':forms.TextInput(attrs={'class':'fname'}),
            'slug':forms.Textarea(attrs={'class':'fname','cols':50,  'rows':1}),
            'teg':forms.Textarea(attrs={'class':'fname','cols':50,  'rows':1}),
            'nomer':forms.NumberInput(attrs={'class':'fname'}),
            'kala':forms.TextInput(attrs={'class':'fname'}),
            'email':forms.EmailInput(attrs={'class':'fname'}),
            'image':forms.ClearableFileInput(attrs={'class':'fname'}),
            'is_published':forms.CheckboxInput(attrs={'class':'fname'}),
                    }

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']