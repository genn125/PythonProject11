from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

'''функция вида, назвали index потому что принимает запрос от клиента 
(отвечает за то, что возвращается при обращении пользователя 
на главную страницу приложения shop)'''

# 1) функция вида
def index(request):
    return HttpResponse('Hello from the Shop app')    #
