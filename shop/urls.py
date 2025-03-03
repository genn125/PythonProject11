from django.urls import path


from  . import views

urlpatterns = [path('', views.index, name='index')]    # Привязка функции вида к определенному маршруту