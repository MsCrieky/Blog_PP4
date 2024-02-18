from django.shortcuts import render

from django.shortcuts import render
from .models import Funfacts


def fun_facts(request):
    """
    Renders the Funfacts page
    """
    funfacts = Funfacts.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "funfacts/funfacts.html",
        {"funfacts": funfacts},
    )

