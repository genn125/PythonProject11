from django.shortcuts import render
from django.http import  HttpResponse

# 23) Изменяем отображение нашей страницы на сайте
# from . import models
from .models import Curse

'''функция вида, назвали index потому что принимает запрос от клиента 
(отвечает за то, что возвращается при обращении пользователя 
на главную страницу приложения shop)'''
'''
# 1) функция вида
#
# def index(request):
#     return HttpResponse('Hello from the Shop app')
#
# 1a) после функцию index необходимо привязать к определенному маршруту в рамках приложения shop
# для этого в папке приложения создаем файл urls.py (в нем будут маршруты только для этого приложения
#

# 23a)
# def index(request):
#     curses = Curse.objects.all()
#     return HttpResponse(curses)

# 25) Используем файл шаблона html, созданного на 24)
'''

def index(request):
   curses = Curse.objects.all()
   return render(request, 'courses.html', {'courses':curses})  # возвращаем результат вызова функции render
# request запрос от клиента, который получает функция index, courses.html - название шаблона

# 26) добавляем 3-й аргумент в render (передаём последовательность curses в функцию render)
# и меняем шаблон, вставляя эту последовательность в шаблон в виде кода python

def single_course(request, course_id):  # 28a) связь с urls.py
   course = Curse.object.get(pk=course_id)  # 28b) ищем 1 курс по ид курса
   return render(request, 'single_course.html', {'course':course})
   # 28) single_course.html - новый шаблон 1 курса и внутри него у нас будет доступ к переменной course




