from django import forms

from .models import Person


class QuickSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    country = forms.ChoiceField(required=False, choices=Person.Countries.choices)
    mobile_number = forms.CharField(max_length=20, required=False)
