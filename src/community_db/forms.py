from django import forms


class QuickSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
