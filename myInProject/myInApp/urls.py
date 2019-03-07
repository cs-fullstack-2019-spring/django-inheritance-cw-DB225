from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),
    path("resources/", views.resources, name="resources"),
    path("contacts/", views.contacts, name="contacts"),
]