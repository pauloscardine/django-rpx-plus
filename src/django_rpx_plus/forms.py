from django import forms

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegisterForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', max_length = 30, label = _('Username'),
                                error_messages={'invalid':_('The username must contain only letters, numbers and underscores.')})
    email = forms.EmailField(label = _('Email Address'), max_length = 254)

    def clean_username(self):
        username = self.cleaned_data['username']
        #Checking to make sure that username is unique.
        try:
            User.objects.get(username = username)
        except User.DoesNotExist:
            #This is good, means that we can use this username:
            return username
        #Otherwise, username exists. We can't use it.
        raise forms.ValidationError(_('Username already exists! Please choose another one.'))
