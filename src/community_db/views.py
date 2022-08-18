from django.db import models
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Person

# FUNCTION BASED VIEWS

# Searching the first name and last name fields
def list_persons_with_template(request):
    search_text = request.GET.get("search")

    persons = Person.objects.all()
    if search_text:
        search_filters = models.Q(first_name__icontains=search_text) | models.Q(
            last_name__icontains=search_text
        )
        persons = persons.filter(search_filters)
    context = {"object_list": persons}
    return render(request, "community_db/person_list_in_base.html", context)


def detail_person_with_template(request, pk):
    person = Person.objects.get(id=pk)
    context = {"object": person}
    return render(request, "community_db/person_detail_in_base.html", context)


# CLASS BASED VIEWS
class PersonListView(ListView):
    model = Person
    template_name = "community_db/person_list_in_base.html"


class PersonDetailView(DetailView):
    model = Person
    template_name = "community_db/person_detail_in_base.html"
