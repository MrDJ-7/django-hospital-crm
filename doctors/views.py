from django.http import HttpResponse

from .models import Doctors


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
