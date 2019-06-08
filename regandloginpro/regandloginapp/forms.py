from django import forms
class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="Enter your first Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'your first name ',
                'class':'form-control'
            }
        )
    )
    last_name=forms.CharField(
        label="Enter your last name ",
        widget=forms.TextInput(
            attrs={
                'placeholder':'your last name',
                'class':'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your mobile number',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label="enter your email id",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'your Email id',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label="enter username",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter your username',
                'class':'form-control'
            }
        )
    )
    password1=forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Enter your password',
                'class':'form-control'
            }
        )
    )
    password2=forms.CharField(
        label="enter your confirmation password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Enter confirmation password',
                'class':'form-control'
            }
        )
    )
class LoginForm(forms.Form):
    username=forms.CharField(
        label="Enter your username",
        widget=forms.TextInput(
            attrs={
                'placeholder':'your username',
                'class':'form-control'
            }
        )
    )
    password1=forms.CharField(
        label="enter your password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'your password',
                'class':'form-control'
            }
        )
    )
