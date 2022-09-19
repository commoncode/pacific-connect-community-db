from django import forms

from .models import Person


class QuickSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        # fields = ["first_name", "last_name", "country", "mobile_number"]
        exclude = []
