from django import forms
from . models import Profile


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']