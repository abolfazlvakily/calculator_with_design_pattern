from django.shortcuts import render
from web.oop import oop


def sum(request, first_number, second_number):
    # sum two numbers on django view
    sum = oop.Sum(first_number, second_number)
    result = sum.execute()
    context = {'sum': result}
    return render(request, 'web/result.html', context)


def subtraction(request, first_number, second_number):
    # subtraction two numbers on django view
    subtraction = oop.Subtraction(first_number, second_number)
    result = subtraction.execute()
    context = {'subtraction': result}
    return render(request, 'web/result.html', context)
