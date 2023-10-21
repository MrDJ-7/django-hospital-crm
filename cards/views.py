from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Cards, Patient
from django.template.response import TemplateResponse
from .card_service import Card_service
import collections


# def index(request):
#     a = Card_service
#     return HttpResponse(a.get_all_doctors())


def get_cards_view(request):
    s = ""
    a = Card_service
    x = a.get_all_doctors()
    for t in x:
        s += str(t.id)
        s += " "
    s += "<br>"
    for t in x:
        s += t.name
        s += " "

    return HttpResponse(s)


# def add_doctor(request):
# name = request.POST.get("doctor_name")
# age = request.POST.get("doctor_age")
# addreass = request.POST.get("doctor_address")
# salary = request.POST.get("doctor_salary")
# if not Doctor_service.doctor_exists(name, age, addreass):
# Doctor_service.add_doctor_data(name, age, addreass, salary)
# message = "doctor succesfuly added"
# else:
# message = "doctor already exist"
#
# return render(request, "add_doctor.html", context={"message": message})
#
#
# def get_add_doctor_form(request):
# return render(request, "add_doctor.html")
#
#
# def get_doctors_json(request):
# docs = {}
# temp = ""
# a = Doctor_service
# doctors_list = a.get_all_doctors()
# for i in doctors_list:
# temp = i.name + " " + str(i.age) + " " + i.address + " " + str(i.salary)
# docs[i.id] = temp
# temp = ""
# return JsonResponse(docs)
#
#
# def doctors_page(request):
# return render(request, "doctors.html")
#
#
# def get_doctors(request):
# doctor_list = Doctor_service
# return JsonResponse(doctor_list.get_all_doctors_map(), safe=False)
#
#
# def get_doctor_json(request, doctor_id):
# a = Doctor_service
# doctor_entry = a.get_doctor(doctor_id)
# doctor_entry_l = [
# doctor_entry.name,
# str(doctor_entry.age),
# doctor_entry.address,
# str(doctor_entry.salary),
# ]
# return JsonResponse(doctor_entry_l, safe=False)
#
#
# def doctor_page(request, doctor_id):
# context = {"doctor_id": doctor_id}
# return render(request, "doctor.html", context)
#
