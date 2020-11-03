from django import forms
from .models import notifications,Business,Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class notificationsForm(forms.ModelForm):
    class Meta:
        model=notifications
        exclude=['author','neighbourhood','post_date']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']
