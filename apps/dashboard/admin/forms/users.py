from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "is_active", "is_verified"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control mx-3 Disabled text-center mb-3'
        self.fields['is_active'].widget.attrs['class'] = 'form-check-input mb-3'
        self.fields['is_verified'].widget.attrs['class'] = 'form-check-input mb-3'
