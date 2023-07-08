from django import forms
from blog_app.models import *
from django.contrib.auth.models import User

class postform(forms.ModelForm):
    class Meta():
        model=post
        fields=("author",'title','text')

        widgets={
            'title':forms.TextInput(attrs={'class':"textinputclass"}),
            'text':forms.Textarea(attrs={'class':"editable medium-editor-textarea postcontent"})
        }


class commentform(forms.ModelForm):
    class Meta():
        model=comment
        fields=("author",'text')

        widgets={
            'author':forms.TextInput(attrs={'class':"textinputclass"}),
            'text':forms.Textarea(attrs={'class':"editable medium-editor-textarea"})
        }

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=("username",'password','first_name','last_name','email',)

class LoginForm(forms.ModelForm):
    class Meta():
        model=login
        fields="__all__"