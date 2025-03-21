from django.urls import path

from  . import views   # импортируем весь модуль views

# 2) Создание этого файла
# 3) и 28) Привязка функции вида к определенному маршруту
urlpatterns = [

    path('', views.index, name='index'),
# "" пустая строка представляет кореневой маршрут приложения,
# views.index ф-ия вида, name= название маршрута

    path('<int:course_id>', views.single_course, name='single_course')
# 28) course_id - имя может быть любым (это параметр маршрута, будем передавать в функцию вида)
# views.single_course - функция вида (будет в файле views)

]

