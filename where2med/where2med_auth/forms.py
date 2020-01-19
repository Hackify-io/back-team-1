from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    password = forms.CharField(
        max_length=24, widget=forms.PasswordInput(attrs={"class": "input"})
    )


class SignupForm_Patient(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input"}))
    password = forms.CharField(
        max_length=24, widget=forms.PasswordInput(attrs={"class": "input"})
    )
    confirm_password = forms.CharField(
        max_length=24, widget=forms.PasswordInput(attrs={"class": "input"})
    )

class SignupForm_MedicalCenter(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "input"})) 
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    city = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    #image = forms.FileField(widget=forms.FileInput())
    cost_per_consult = forms.DecimalField(widget=forms.NumberInput())

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "input"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input"}))
    password = forms.CharField(
        max_length=24, widget=forms.PasswordInput(attrs={"class": "input"})
    )
    confirm_password = forms.CharField(
        max_length=24, widget=forms.PasswordInput(attrs={"class": "input"})
    )
