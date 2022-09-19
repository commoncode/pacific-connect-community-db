"""pacificconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from community_db import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("check-my-auth/", views.check_my_auth),
    path("fbv/people/", views.list_persons_with_template, name="fbv-person-list"),
    path(
        "fbv/people/<int:pk>/",
        views.detail_person_with_template,
        name="fbv-person-detail",
    ),
    path(
        "fbv/people/<int:pk>/edit/",
        views.edit_person_with_template,
        name="fbv-person-edit",
    ),
    path("cbv/people/", views.PersonListView.as_view(), name="cbv-person-list"),
    path(
        "cbv/people/<int:pk>/",
        views.PersonDetailView.as_view(),
        name="cbv-person-detail",
    ),
    path(
        "cbv/people/<int:pk>/edit/",
        views.PersonUpdateView.as_view(),
        name="cbv-person-edit",
    ),
    path("accounts/login/", views.UserLoginView.as_view(), name="login"),
]
