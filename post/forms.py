from django import forms
from django.forms.widgets import CheckboxSelectMultiple, TextInput, Textarea
from . models import Post, Comment, Reply


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'forum']
        labels = {
            'categories': 'Choose Categorie*',
            'topic': 'Topic*',
            'content': 'Comment*'
        }
        widgets = {
            'categories': CheckboxSelectMultiple,
            'topic': TextInput(attrs={'placeholder': "Topic...", 'class': 'form-control'}),
            'content': Textarea(attrs={'placeholder': "Comment here...", 'class': 'form-control'})
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'forum']
        labels = {
            'categories': 'Edit Categorie*',
            'topic': 'Edit Topic*',
            'content': 'Edit Comment*'
        }
        widgets = {
            'categories': CheckboxSelectMultiple,
            'topic': TextInput(attrs={'placeholder': "Topic...", 'class': 'form-control'}),
            'content': Textarea(attrs={'placeholder': "Comment here...", 'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Comment*'
        }
        widgets = {
            'content': Textarea(attrs={'placeholder': "Make a comment...", 'class': 'form-control'})
        }

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Edit Comment*'
        }
        widgets = {
            'content': Textarea(attrs={'placeholder': "Make a comment...", 'class': 'form-control'})
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': 'Reply*'
        }
        widgets = {
            'content': Textarea(attrs={'placeholder': "Reply here...", 'class': 'form-control'})
        }

class ReplyUpdateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': 'Edit Reply*'
        }
        widgets = {
            'content': Textarea(attrs={'placeholder': "Reply here...", 'class': 'form-control'})
        }



