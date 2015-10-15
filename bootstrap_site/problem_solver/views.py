from django.shortcuts import render

from .forms import CapitaliseForm, ArabicNumeralsForm

def index(request):
    return render(request, 'index.html')

def capitalise(request):
    form = CapitaliseForm(request.POST or None)
    context = {
        "form": form,
    }

    if form.is_valid():
        example_text = form.cleaned_data.get("text")
        example_text = " ".join([word[0].upper() + word[1:] \
                                for word in example_text.split()])
        context = {
            "form": form,
            "capitalised_text": example_text,
        }

    return render(request, 'capitalise.html', context)


import roman

def arabic_numerals(request):
    form = ArabicNumeralsForm(request.POST or None)
    context = {
        "form": form,
    }

    if form.is_valid():
        numerals = form.cleaned_data.get("roman_numerals")

        try:
            numerals = roman.fromRoman(numerals.upper())
        except:
            numerals = "unable to convert: " + \
                       form.cleaned_data.get("roman_numerals")

        context = {
            "form": form,
            "arabic_numerals": numerals,
        }

    return render(request, 'arabic_numerals.html', context)