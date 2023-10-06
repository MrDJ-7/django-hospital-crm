from django.shortcuts import render


def for_error_404(request):
    return render(request, "error.html")
