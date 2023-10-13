from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Doctors
from django.template.response import TemplateResponse
from .doctor_service import Doctor_service
import collections


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# # Leave the rest of the views (detail, results, vote) unchanged

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
# from django.http import HttpResponse


def index(request):
    # x = "Hello, world.! You're at the polls index."
    a = Doctor_service
    # b = Doctors.objects.get(id=1)
    # b = ""
    # for x in a:
    #     print(x.name)
    return HttpResponse(a.get_all_doctors())


def get_doctor_view(request):
    s = ""
    a = Doctor_service
    x = a.get_all_doctors()
    for t in x:
        s += str(t.id)
        s += " "
    s += "<br>"
    for t in x:
        s += t.name
        s += " "

    return HttpResponse(s)


def add_doctor(request):
    # print(request.POST)
    print(Doctor_service.doctor_exists("cal", 2, "Grostreet 201"))

    return HttpResponse()


def get_add_doctor_form(request):
    return render(request, "add_doctor.html")


def get_doctors_json(request):
    docs = {}
    temp = ""
    a = Doctor_service
    doctors_list = a.get_all_doctors()
    for i in doctors_list:
        temp = i.name + " " + str(i.age) + " " + i.address + " " + str(i.salary)
        docs[i.id] = temp
        temp = ""
    return JsonResponse(docs)

    # if request.method == "GET":
    #     return HttpResponse("Success!")  # Sending an success response
    # else:
    #     return HttpResponse("Request method is not a GET")


def doctors_page(request):
    return render(request, "doctors.html")


def get_doctors(request):
    doctor_list = Doctor_service
    # doctors_list.get_all_doctors_map()
    return JsonResponse(doctor_list.get_all_doctors_map(), safe=False)


# def add_task(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         task = Doctors.objects.create(title=title)
#         return JsonResponse({"status": "success"})


def get_doctor_json(request, doctor_id):
    # id = 1
    a = Doctor_service
    doctor_entry = a.get_doctor(doctor_id)
    # to do: redo as serializer
    #
    #
    doctor_entry_l = [
        doctor_entry.name,
        str(doctor_entry.age),
        doctor_entry.address,
        str(doctor_entry.salary),
    ]
    return JsonResponse(doctor_entry_l, safe=False)


def doctor_page(request, doctor_id):
    # doctor_id = request.GET.get("doctor_id", "")
    context = {"doctor_id": doctor_id}
    # return TemplateResponse(request, "doctor.html", {doctor_id: doctor_id})
    return render(request, "doctor.html", context)
