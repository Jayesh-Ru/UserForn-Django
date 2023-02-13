from django import forms
from .models import UserDetails
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import DateInput, SelectDateWidget
import phonenumbers


class RegistrationForm(forms.ModelForm):

    name = forms.CharField(
        label='Enter Username', min_length=4, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required')
    phonenumber = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': _('Phone')}),
        label=_("Phone number"), required=True, region='IN')
    dob = forms.DateField(
        label='Date of Birth(DOB)',
        widget=SelectDateWidget(years=range(1900, 2023), empty_label=(
            "Choose Year", "Choose Month", "Choose Day"),
        ))

    class Meta:
        model = UserDetails
        fields = ('name', 'email', 'phonenumber', 'dob')
        widgets = {
            'phonenumber': PhoneNumberPrefixWidget(initial='IN'),
            'dob': DateInput(format=["%Y-%m-%d"],),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phonenumber")
        z = phonenumbers.parse(phone_number, "IN")
        if not phonenumbers.is_valid_number(z):
            raise forms.ValidationError("Number not in Indian format")
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3 name', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3 id_email', 'placeholder': 'E-mail',
             'name': 'email'})
        self.fields['dob'].widget.attrs.update(
            {'placeholder': '20/09/1999', 'name': 'dob', 'class': 'dob'})
