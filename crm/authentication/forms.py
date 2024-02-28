from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class FormRegister(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password")

    def save(self, commit=True):
        user = super(FormRegister, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
