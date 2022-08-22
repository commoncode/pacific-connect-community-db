from django import forms


class QuickSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)


class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100, required=False)
    mobile_number = forms.CharField(max_length=20, required=False)
