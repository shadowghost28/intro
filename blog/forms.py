from django import forms   #el modelo Post lo traemos aqui para manipular

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content')  #llevamos este modelo a la Vista 
