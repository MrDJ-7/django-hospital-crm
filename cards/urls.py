from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("cards_1/", views.get_cards_view, name="get_cards_view"),
]
