from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

# Create your views here.


def home_view(*args, **kwargs):
    return HttpResponse("<h1>This is my first view!<h1/>")


@api_view(['GET'])
def get_names_view(request):
    names = ["alex", "franchelou", "moubala"]
    return JsonResponse({"names": names})

