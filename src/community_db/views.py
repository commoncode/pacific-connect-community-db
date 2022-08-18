from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Person

# FUNCTION BASED VIEWS


def list_persons_with_template(request):
    persons = Person.objects.all()
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
