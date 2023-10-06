from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("doctors/", views.get_doctor_view, name="get_doctor_view"),
    path("doctors_page/", views.doctors_page, name="doctors_page"),
    path("get_doctors_json/", views.get_doctors_json, name="get_doctors_json"),
    path("add_doctor/", views.get_doctors_json, name=" "),
    path("doctor_page/", views.doctor_page, name="doctor_page"),
    path("get_doctor_json/", views.get_doctor_json, name="get_doctor_json"),
]
