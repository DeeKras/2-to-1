from django import forms
from django.contrib.auth.models import User

import hashlib

class AuthenticationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.widgets.TextInput, label="User Name")
    password = forms.CharField(widget=forms.widgets.PasswordInput, label="password")

    class Meta:
        model = User
        fields = ['username', 'password', ]

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.widgets.TextInput, label="User Name")
    email = forms.EmailField(widget=forms.widgets.TextInput, label="Email")
    password1 = forms.CharField(widget=forms.widgets.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.widgets.PasswordInput, label="password (again)")
    first_name = forms.CharField(widget=forms.widgets.TextInput, label="First Name")
    last_name = forms.CharField(widget=forms.widgets.TextInput, label="Last Name")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')

    def clean(self):
        print 'cleaning'
        self.cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        print 'saving'
        user = super(RegistrationForm, self).save(commit=False)
        # hashed_password = hashlib.md5(self.cleaned_data['password1']).hexdigest()
        # user.password = hashed_password
        if commit:
            user.save()
        return user


