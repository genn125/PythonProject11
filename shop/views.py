from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse, Http404
# 23) Изменяем отображение нашей страницы на сайте
from .models import Course
'''функция вида, назвали index потому что принимает запрос от клиента (отвечает за то, что возвращается 
 при обращении пользователя на главную страницу приложения shop)
1) функция вида: 1a) после функцию index необходимо привязать к определенному маршруту в рамках приложения shop
для этого в папке приложения создаем файл urls.py (в нем будут маршруты только для этого приложения
   def index(request):
      return HttpResponse('Hello from the Shop app')
23a)def index(request):
      curses = Course.objects.all()
      return HttpResponse(courses)'''
#25) Используем файл шаблона html, созданного на 24)
def index(request):
   courses = Course.objects.all()
   return render(request, 'courses.html', {'courses':courses})  # возвращаем результат вызова функции render
# request запрос от клиента, который получает функция index, courses.html - название шаблона
# 26) добавляем 3-й аргумент в render (передаём последовательность courses в функцию render)
# и меняем шаблон courses.html, вставляя эту последовательность в шаблон <tbody> в виде кода python

def single_course(request, course_id):  # 29a) связь с urls.py

# 31) Отображение страницы 404 ВАРИАНТ 1: (try except)
#    try:
#       course = Course.objects.get(pk=course_id)  # 29b) ищем 1-й курс по id курса (записали это в urls.py)
#       return render(request, 'single_course.html', {'course': course})
#       # 29) single_course.html - новый шаблон (страница) одного курса и внутри него у нас будет доступ к переменной course
#    except Course.DoesNotExist:
#       raise Http404()

# 31) Отображение страницы 404 ВАРИАНТ 2: (Импорт функции get_object_or_404)

   course = get_object_or_404(Course, pk=course_id)
   return render(request, 'single_course.html', {'course': course})


