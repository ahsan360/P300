from django import forms
 
from django.contrib.auth.models import User
from . models import Add, Hello,Add2,Add3,Hello2,Hello3
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1' ,'password2']

class GeeksForm(forms.ModelForm):
    
    
    # create meta class
    class Meta:
        # specify model to be used
        model = Add
  
        # specify fields to be used
        fields = ['title', 'author',  'body']
  
        widget = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.TextInput(attrs={'class':'form-control'}),
       }
class GeeksForm2(forms.ModelForm):
    
    
    # create meta class
    class Meta:
        # specify model to be used
        model = Add2
  
        # specify fields to be used
        fields = ['title', 'author',  'body']
  
        widget = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.TextInput(attrs={'class':'form-control'}),
       }
class GeeksForm3(forms.ModelForm):
    
    
    # create meta class
    class Meta:
        # specify model to be used
        model = Add3
  
        # specify fields to be used
        fields = ['title', 'author',  'body']
  
        widget = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.TextInput(attrs={'class':'form-control'}),
       }

class comment(forms.ModelForm):
    
    
    # create meta class
    class Meta:
        # specify model to be used
        model = Hello
  
        # specify fields to be used
        fields = ['body','image']
  
        widget = {
             
            'body' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
       }
class comment2(forms.ModelForm):
    
    
    # create meta class
    class Meta:
        # specify model to be used
        model = Hello2
  
        # specify fields to be used
        fields = ['body','image']
  
        widget = {
             
            'body' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
       }
class comment3(forms.ModelForm):
    
    
    # create meta class
    class Meta:
        # specify model to be used
        model = Hello3
  
        # specify fields to be used
        fields = ['body','image']
  
        widget = {
             
            'body' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
       }