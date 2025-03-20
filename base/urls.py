"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # это делаем сами, затем 4)

urlpatterns = [
    path('admin/', admin.site.urls),

# 4) Включаем Все маршруты из файла shop\urls.py, они будут доступны тут
    path('shop/', include('shop.urls'))
# 'shop/' маршрут ведет в приложение shop, include('shop.urls') - включить все маршруты shop.urls
]
''' После 'shop/' могут быть course/10  или categories, которые настраиваются в файле 'shop.urls'
'''



