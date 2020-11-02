from django import forms
from .models import notifications,Business,Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']
