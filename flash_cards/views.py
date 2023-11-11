from django.shortcuts import render


def flash_cards_home(request):
    return render(request, "flash_cards/flash.html")
