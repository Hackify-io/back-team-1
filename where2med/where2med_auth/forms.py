from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input"}))
    password = forms.CharField(
        max_length=24, widget=forms.PasswordInput(attrs={"class": "input"})
    )


class SignupForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input"}))
    password = forms.CharField(
        max_length=24, widget=forms.PasswordInput(attrs={"class": "input"})
    )
    confirm_password = forms.CharField(
        max_length=24, widget=forms.PasswordInput(attrs={"class": "input"})
    )
