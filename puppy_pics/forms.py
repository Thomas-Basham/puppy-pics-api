from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.admin.forms import AdminAuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django import forms


# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email'].lower()
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'someone@email.com', 'for': 'Email'}
    ),
        label=_("Email")

    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
        }
    ))


class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    """
    A custom authentication form used in the admin app.
    """
    error_messages = {
        **AuthenticationForm.error_messages,
        'invalid_login': _(
            "Please enter the correct phone number or email and password for a staff "
            "account. Note that both fields may be case-sensitive."
        ),
    }

    username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
