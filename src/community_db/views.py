from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.list import ListView

from community_db.models import Person


def list_persons(request):
    html = "<html><body>This is my list of folks<ul>"

    for person in Person.objects.all():
        html += f"<li>{person.first_name} {person.last_name} from {person.country}</li>"

    html += "</ul></body></html>"
    return HttpResponse(html)


# def list_persons_with_template(request):
#     persons = Person.objects.all()
#     template = loader.get_template("community_db/person_list.html")
#     context = {"object_list": persons}
#     return HttpResponse(template.render(context, request))


def list_persons_with_template(request):
    persons = Person.objects.all()
    template = loader.get_template("community_db/person_list_in_base.html")
    context = {"object_list": persons}
    return HttpResponse(template.render(context, request))


# def list_persons_with_template(request):
#     persons = Person.objects.all()
#     context = {"object_list": persons}
#     return render(request, "community_db/person_list.html", context)


class PersonListView(ListView):
    model = Person
    template_name = "community_db/person_list_in_base.html"
