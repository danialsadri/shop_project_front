from django import forms
from .models import ContactModel, NewsLetterModel


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["full_name", "email", "phone_number", "subject", "content"]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'formFirstName'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'formEmail'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'formPhoneNumber'}),
            'subject': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'formSubject'}),
            'content': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 4, 'id': 'formDescription'}),
        }

        error_messages = {
            'full_name': {'required': "فیلد نام و نام خانوادگی نمی تواند خالی باشد"},
            'email': {'required': "فیلد ایمیل نمی تواند خالی باشد"},
            'phone_number': {'required': "فیلد شماره تلفن نمی تواند خالی باشد"},
            'subject': {'required': "فیلد  عنوان نمی تواند خالی باشد"},
            'content': {'required': "فیلد محتوا نمی تواند خالی باشد"},
        }


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterModel
        fields = ['email']
