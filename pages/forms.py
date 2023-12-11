from django import forms
from .models import Posts


class PostForm(forms.ModelForm):
    slug = forms.SlugField(required=False)

    class Meta:
        model = Posts
        fields = '__all__'
        exclude = ['author']
