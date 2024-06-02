from django.contrib.auth import forms as auth_forms


class AuthenticationForm(auth_forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(AuthenticationForm, self).confirm_login_allowed(user)
