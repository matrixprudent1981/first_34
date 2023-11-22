from django.shortcuts import render
from django.shortcuts import HttpResponse, render
import datetime
from post.models import Product



def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all() # May be here error!
        # for product in products:
        #     print(product.title)
        #     print(product.name)
        #     print(product.description)
    return render(request, 'products/main.html', context={'products': products}) #  значение product

def hello_view(request):
   #print(request.method)
    if request.method == 'GET':
        return render(request, 'index.html')

#  Почему у меня не отображается print(request)!!! Ответ получил, что бы он работал надо, именно тот view должен быть активировано


def good_bye(request):
    if request.method == 'GET':
        return render(request, 'index_goodbye.html')


def current_date(request):
    if request.method == 'GET':
        return HttpResponse(f'Настоящее дата и время: {datetime.datetime.now()}')



def test(request):
    if request.method == 'GET':
        return HttpResponse('TEST!')

