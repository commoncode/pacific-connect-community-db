from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView, redirect_to_login
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from .forms import PersonForm, PersonSearchForm
from .models import Person

# FUNCTION BASED VIEWS

# Searching the first name and last name fields with text in the search box
def list_persons_with_template(request):
    search_text = request.GET.get("search")

    persons = Person.objects.all()
    if search_text:
        search_filters = models.Q(first_name__icontains=search_text) | models.Q(
            last_name__icontains=search_text
        )
        persons = persons.filter(search_filters)
    context = {"object_list": persons, "search_text": search_text}
    return render(request, "community_db/person_list_in_base.html", context)


def detail_person_with_template(request, pk):
    person = get_object_or_404(Person, id=pk)
    context = {"object": person}
    return render(request, "community_db/person_detail_in_base.html", context)


@login_required
def edit_person_with_template(request, pk):
    person = get_object_or_404(Person, id=pk)

    if not person.users.contains(request.user):
        return redirect_to_login(request.path)

    if request.POST:
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("fbv-person-detail", args=[person.id]))
    else:
        form = PersonForm(instance=person)
    context = {"object": person, "form": form}
    return render(request, "community_db/person_form_in_base.html", context)


def search_persons_with_template_AND(request):
    if request.GET:
        search_form = PersonSearchForm(request.GET)
        show_results = True

        persons = Person.objects.all()
        search_form.is_valid()
        cleaned_data = search_form.cleaned_data
        if cleaned_data.get("first_name"):
            persons = persons.filter(first_name__icontains=cleaned_data["first_name"])
        if cleaned_data.get("last_name"):
            persons = persons.filter(last_name__icontains=cleaned_data["last_name"])
        if cleaned_data.get("country"):
            persons = persons.filter(country=cleaned_data["country"])
        if cleaned_data["mobile_number"]:
            persons = persons.filter(
                mobile_number__icontains=cleaned_data["mobile_number"]
            )

        allowed_sort_options = ("first_name", "last_name", "country", "mobile_number")
        if cleaned_data.get("sort_by") in allowed_sort_options:
            persons = persons.order_by(cleaned_data["sort_by"])
    else:
        search_form = PersonSearchForm()
        show_results = False
        persons = Person.objects.none()

    context = {
        "object_list": persons,
        "form": search_form,
        "show_results": show_results,
    }
    return render(request, "community_db/person_search_form.html", context)


def search_persons_with_template_OR(request):
    search_form = PersonSearchForm(request.GET)

    search_form.is_valid()
    cleaned_data = search_form.cleaned_data
    search_filters = models.Q()
    if cleaned_data.get("first_name"):
        search_filters &= models.Q(first_name__icontains=cleaned_data["first_name"])
    if cleaned_data.get("last_name"):
        search_filters &= models.Q(last_name__icontains=cleaned_data["last_name"])
    if cleaned_data.get("country"):
        search_filters &= models.Q(country=cleaned_data["country"])
    if cleaned_data["mobile_number"]:
        search_filters &= models.Q(
            mobile_number__icontains=cleaned_data["mobile_number"]
        )

    persons = Person.objects.filter(search_filters)

    context = {"object_list": persons, "form": search_form}
    return render(request, "community_db/person_search_form.html", context)


# CLASS BASED VIEWS
class PersonListView(ListView):
    model = Person
    template_name = "community_db/person_list_in_base.html"

    def get_queryset(self):
        # Get the default queryset - i.e. set of rows - that we want
        # to filter
        queryset = super().get_queryset()

        # Get the search field value - but from self.request in the
        # class based view
        search_text = self.request.GET.get("search")

        # Filter if we need to
        if search_text:
            search_filters = models.Q(first_name__icontains=search_text) | models.Q(
                last_name__icontains=search_text
            )
            queryset = queryset.filter(search_filters)

        # Return the queryset now that we have filtered it (if we need to)
        return queryset

    def get_context_data(self, **kwargs):
        # Get the default context that would be generated
        context = super().get_context_data(**kwargs)

        # Get the search text and add it to the context
        search_text = self.request.GET.get("search")
        context["search_text"] = search_text

        # Return our new context
        return context


class PersonDetailView(DetailView):
    model = Person
    template_name = "community_db/person_detail_in_base.html"


class PersonUpdateView(UpdateView):
    model = Person
    fields = ["first_name", "last_name", "country", "mobile_number"]
    template_name = "community_db/person_form_in_base.html"

    def get_success_url(self):
        return reverse("cbv-person-detail", args=[self.object.id])


def check_my_auth(request):
    output = ["<html><body>"]
    output.append(f"Is anonymous: {request.user.is_anonymous}")
    output.append(f"Is authenticated: {request.user.is_authenticated}")
    output.append(f"Username: {request.user.username}")
    output.append("</body></html>")
    return HttpResponse("<br>".join(output))


class UserLoginView(LoginView):
    template_name = "cbv-login-form.html"

    def get_default_success_url(self):
        return reverse("cbv-person-list")
