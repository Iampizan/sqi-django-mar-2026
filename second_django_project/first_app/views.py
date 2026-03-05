from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def corect_code(request):
    return HttpResponse("This code is very correct with no bug")

def not_correct_code(request):
    return HttpResponse("this code is not a correct code it has a lot of bugs ")