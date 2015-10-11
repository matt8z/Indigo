#!/usr/bin/env python3
from .models import UserProfile
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_email(self):
    	email = self.cleaned_data.get('email')
    	first, second = email.split("@")

    	if not second == "student.dist113.org":
    		raise forms.ValidationError("Please use a District 113 email")

    	return email