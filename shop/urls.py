from django.urls import path

from  . import views   # импортируем весь модуль views

# 3) Привязка функции вида к определенному маршруту
urlpatterns = [path('', views.index, name='index')]  # views.index ф-ия вида, name= название маршрута