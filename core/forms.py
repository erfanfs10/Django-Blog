from django import forms
from .models import Post, Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "title"}),
            'body': forms.Textarea(attrs={'placeholder': 'body'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
