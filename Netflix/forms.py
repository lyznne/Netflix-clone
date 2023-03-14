from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    """ Registration form  class """

    firstname = forms.CharField(label="First name")
    lastname = forms.CharField(label="Last name")
    email = forms.EmailField(label="Email address")
    password = forms.CharField(label="Password", widget=forms.PasswordInput(render_value=True), min_length=6)
    passwordconf = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)


    def clean(self):
        """"check if the password matches the confirmation """
        super(RegisterForm, self).clean()

        # extract user input data
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_conf = self.cleaned_data.get('password_conf')

        #check if the password match
        if password != password_conf:
            self._errors['password_conf'] = self.error_class([
                "Password does not match !"
            ])

        # check if email exist
        if User.objects.filter(username=email).exists():
            self._errors['email'] = self.error_class([
                "Email already exist "
            ])
        
        # return errors if found
        return self.cleaned_data
        
class LoginForm(forms.Form):
    """" login form class """
    email = forms.EmailField(label="Email address")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SearchForm(forms.Form):
    """ search form class"""
    search_text = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search'})
    )