from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Funfacts

class FunfactsList(generic.ListView):
    """
    Returns all published posts in :model:`funfacts.Funfacts`
    and displays them in a page of three posts. 
    **Context**

    ``queryset``
        All published instances of :model:`funfacts.Funfacts`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`funfacts/funfacts.html`
    """
    queryset = Funfacts.objects.all()
    template_name = "funfacts/funfacts.html"
    paginate_by = 9

def fun_facts(request, slug):
    funfacts = Funfacts.objects.all().order_by('-updated_on').first()

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(request, "funfacts/funfacts.html",
        {
            "post": post,
            "rating": rating,
        },
    )
    