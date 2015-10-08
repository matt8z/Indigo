#!/usr/bin/env python3
from .models import UserProfile
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = (email, username, password)