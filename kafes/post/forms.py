from django import forms
from .models import Post, Comment


#django da fromları class türünde tanımlıyoruz.

class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',



        ]
        #formu tanımladık



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]