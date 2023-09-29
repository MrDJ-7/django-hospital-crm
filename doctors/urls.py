from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("doctors", views.get_doctor_view, name="get_doctor_view"),
]
