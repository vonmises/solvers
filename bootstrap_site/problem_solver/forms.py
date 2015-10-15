from django import forms

class CapitaliseForm(forms.Form):
    text = forms.CharField()
