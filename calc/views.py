from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'chima'})


def add(request):

    val1 = int(request.POST["num1"])
    val2 = int (request.POST["num2"])
    res = val1 + val2


    return render(request, 'result.html', {'result': res})

def sub(request):

    num1 = int(request.POST["sub1"])
    num2 = int(request.POST["sub2"])
    res = num1 - num2
    return render(request, 'subtract.html', {"result": res})