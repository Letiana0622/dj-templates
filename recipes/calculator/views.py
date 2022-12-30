from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, reverse
import pytz
from datetime import datetime
import os

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_name = 'home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать рецепт омлета': reverse('omlet'),
        'Показать рецепт пасты': reverse('pasta'),
        'Показать рецепт сендвича': reverse('buter'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def omlet_view(request):
    DATA_omlet = DATA['omlet']
    msg = {}
    template_name = 'recipe.html'
    name = 'омлета'
    servings = int(request.GET.get('servings',1))
    for k, v in DATA_omlet.items():
        v_servings = v * servings
        msg[k] = v_servings
    context = {
        'msg': msg
    }
    return render(request, template_name, context)

def pasta_view(request):
    DATA_pasta = DATA['pasta']
    msg = {}
    template_name = 'recipe.html'
    servings = int(request.GET.get('servings', 1))
    for k, v in DATA_pasta.items():
        v_servings = v * servings
        msg[k] = v_servings
    context = {
        'msg': msg
    }
    return render(request, template_name, context)

def buter_view(request):
    DATA_buter = DATA['buter']
    msg = {}
    template_name = 'recipe.html'
    servings = int(request.GET.get('servings', 1))
    for k, v in DATA_buter.items():
        v_servings = v * servings
        msg[k] = v_servings
    context = {
        'msg': msg
    }
    return render(request, template_name, context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }