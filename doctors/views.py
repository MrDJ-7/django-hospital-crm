from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Doctors
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
    a = Doctors.objects.all()
    # b = Doctors.objects.get(id=1)
    # b = ""
    # for x in a:
    #     print(x.name)
    return HttpResponse(a)


def get_doctor_view(request):
    s = ""
    x = Doctors.objects.all()
    for t in x:
        s += str(t.id)
        s += " "
    s += "<br>"
    for t in x:
        s += t.name
        s += " "

    return HttpResponse(s)


def add_doctor(request):
    pass


def get_doctors_json(request):
    docs = {}
    temp = ""
    doctors_list = Doctors.objects.all()
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
    doctors_l = Doctors.objects.all()
    doctors_list = [
        {"id": doctors_temp.id, "name": doctors_temp.name} for doctors_temp in doctors_l
    ]
    return JsonResponse(doctors_list, safe=False)


# def add_task(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         task = Doctors.objects.create(title=title)
#         return JsonResponse({"status": "success"})
