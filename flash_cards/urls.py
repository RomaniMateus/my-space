from django.urls import path

from flash_cards.views import flash_cards_home

urlpatterns = [
    path("", flash_cards_home, name="flash_cards_home"),
]
