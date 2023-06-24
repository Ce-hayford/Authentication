from dataclasses import field
from .models import signUser
from django import forms

class UserformAPI(forms.ModelForm):
    # email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = signUser
        fields = ['email','password']



class UserRegisterAPI(forms.ModelForm):
    # firstname= forms.CharField(max_length=32)
    # lastname= forms.CharField(max_length=64)
    # email = forms.EmailField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = signUser
        fields = ['firstname', 'lastname', 'username', 'email', 'password']


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)



class passwordChangeView(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)

    model = signUser
    fields = ['password', 'confirmPassword']



class resetPassword(forms.ModelForm):
    email = forms.EmailField(max_length=200)

    model = signUser
    fields = ['email']