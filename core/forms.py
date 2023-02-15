from django import forms
from .models import Post, Profile
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        # widgets = {
        #     'title': forms.TextInput(attrs={'placeholder': _("title")}),
        #     'body': forms.Textarea(attrs={'placeholder': _('body')}),
        # }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']
