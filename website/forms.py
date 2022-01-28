from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import CharField
from django.forms.widgets import TextInput

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    class Meta:
        username = CharField(widget=TextInput(attrs={'id': 'usn'}))
        model = User
        fields = ['username', 'email', 'password1', 'password2']