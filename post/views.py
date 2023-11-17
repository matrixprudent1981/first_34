from django.shortcuts import render
from django.shortcuts import HttpResponse, render
import datetime


def hello_view(request):
   #print(request.method)
    if request.method == 'GET':
        return render(request, 'index.html')

#  Почему у меня не отображается print(request)!!!


def good_bye(request):
    if request.method == 'GET':
        return render(request, 'index_goodbye.html')


def current_date(request):
    if request.method == 'GET':
        return HttpResponse(f'Настоящее дата и время: {datetime.datetime.now()}')


def test(request):
    if request.method == 'GET':
        return HttpResponse('TEST!')

