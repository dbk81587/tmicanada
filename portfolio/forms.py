from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from portfolio.models import Board
from django.forms import ModelForm
from django.utils import timezone

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'First_name(Optional)','autofocus':'autofocus'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Last_name(Optional)'}))
    username = forms.CharField(min_length=5, max_length=20, widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'Username'}),)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control input-lg','placeholder':'email'}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control input-lg','placeholder':'password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class':'form-control input-lg','placeholder':'password confirmtion'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

class WritePostForm(ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'autofocus':'autofocus'}))
    memo = forms.CharField(required=True, widget=forms.Textarea)
    class Meta:
        model = Board
        labels = {
        "memo": "Text"
        }
        fields = ('name', 'location', 'title', 'memo')