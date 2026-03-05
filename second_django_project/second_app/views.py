from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def second_correct_code(request):
    return HttpResponse("This is the second correct code")

def second_incorrect_code(request):
    return HttpResponse("This is the second incorrect line of code")
