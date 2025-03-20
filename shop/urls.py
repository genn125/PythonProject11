from django.urls import path

from  . import views   # импортируем весь модуль views

# 2) Создание этого файла
# 3) Привязка функции вида к определенному маршруту
urlpatterns = [path('', views.index, name='index')]  # "" пустая строка представляет кореневой маршрут приложения,
                                                     # views.index ф-ия вида, name= название маршрута