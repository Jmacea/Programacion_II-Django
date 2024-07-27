from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "username"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "id": "password"
            }
        )
    )
    
class UserForm(UserCreationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username"
                
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "last_name"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "first_name"
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "id": "password1"
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "id": "password2"
            }
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
                "id": "email"
            }
        )
    )
    
    photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'type': 'file',
                'class': 'form-control',
                'id': 'photo'
                }
            )
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'username', 'photo')
        
class UserEditForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username"
                
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "last_name"
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "first_name"
            }
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': 'email',
                'class': 'form-control',
                "id": "email"
            }
        )
    )
    
    photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'type': 'file',
                'class': 'form-control',
                'id': 'photo'
                }
            )
    )
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'photo')