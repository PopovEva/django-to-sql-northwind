from django.shortcuts import render
from django.http import JsonResponse
# from .models import Car
def index(req):
    return JsonResponse('hello', safe=False)


