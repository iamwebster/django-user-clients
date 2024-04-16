from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password1',
            'password2',
        )

    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()