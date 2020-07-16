from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def show_maps(request):
    return render(request, 'maps.html')
