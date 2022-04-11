
from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
import random


def calculator(request):

    # 1.데이터 확인
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = num1 + num2
    elif operators == '-':
        result = num1 - num2
    elif operators == '*':
        result = num1 * num2
    elif operators == '/':
        result = num1 / num2
    else:
        result = 0

    # 3. 응답
    return render(request, 'calculator.html', {'result': result})


def lotto(request):
    list = range(1, 45)
    lotto = random.sample(list, 7)
    # print(lotto)
    return render(request, 'lotto.html', {'lotto': lotto})
