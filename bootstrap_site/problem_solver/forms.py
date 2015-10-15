from django import forms

class CapitaliseForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput({
            "class": "form-control",
            "placeholder": "text to capitalise",
            }))
