from django import forms

from .models import Person


class QuickSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "country", "mobile_number"]


class PersonSearchForm(forms.Form):
    COUNTRIES = [("", "")] + list(Person.Countries.choices)

    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    country = forms.ChoiceField(required=False, choices=COUNTRIES)
    mobile_number = forms.CharField(max_length=20, required=False)
