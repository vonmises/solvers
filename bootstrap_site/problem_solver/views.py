from django.shortcuts import render

from .forms import CapitaliseForm

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